import re

from models import EnumManager
from parsers import ParserCSV, ParserJSON, ParserXML


class InputManger:
    def __init__(self, path):
        self.path = path
        regex_pattern = r"\.(\w+)$"

        extension = re.search(regex_pattern, path)
        self.extension = extension.group(1) if extension else None

    def get_reader(self):
        if self.extension in EnumManager.CSV:
            return self._read_csv()
        elif self.extension in EnumManager.XML:
            return self._read_xml()
        elif self.extension in EnumManager.JSON:
            return self._read_json()
        else:
            raise Exception(f"Expecting csv/xml/json extension. Got '{self.extension}'")

    def _read_csv(self):
        return ParserCSV(self.path)

    def _read_json(self):
        return ParserJSON()

    def _read_xml(self):
        return ParserXML()
