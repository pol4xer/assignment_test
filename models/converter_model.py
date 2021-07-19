from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class UnifiedFields:
    date: Any = None
    from_id: int = None
    to_id: int = None
    transaction_type: str = None
    amount: float = None


class UnifiedConvertor:
    def __init__(self, bank_config):
        self.bank_config = bank_config

    def convert(self, data: dict):
        unified = UnifiedFields()
        bank_config = self.bank_config

        if bank_config.amount_fraction_field:
            unified.amount = float(
                f"{data[bank_config.amount_field]}.{data[bank_config.amount_fraction_field]}"
            )
        else:
            unified.amount = float(data[bank_config.amount_field])

        unified.date = datetime.strptime(data[bank_config.date_field], bank_config.date_format)

        unified.transaction_type = data[bank_config.type_field]

        unified.from_id = data[bank_config.from_field]
        unified.to_id = data[bank_config.to_field]

        return unified
