from dataclasses import dataclass
from typing import List


@dataclass
class Bank:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__()

    bank_name: str = None
    files_path: List[str] = None

    date_field: str = None
    date_format: str = None

    type_field: str = None

    amount_field: str = None
    amount_fraction_field: str = None

    from_field: str = None
    to_field: str = None
