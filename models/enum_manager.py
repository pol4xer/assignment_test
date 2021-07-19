from enum import Enum


class EnumManager(Enum):
    CSV = "csv"
    JSON = "json"
    XML = "xml"
    MONGO = "mongo"
    SQL = "sql"

    def __get__(self, instance, owner):
        return self.value
