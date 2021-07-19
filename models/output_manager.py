import csv

from models.enum_manager import EnumManager


class OutputManager:
    def __init__(self, output_infos: list):
        self.buffer = list()
        self.save_file_manager = dict()

        values = [EnumManager.CSV, EnumManager.JSON, EnumManager.XML]
        for output_info in output_infos:
            if output_info['type'].lower() in values:
                file_path = f"{output_info['path']}{output_info['name']}.{output_info['type']}"
                self.save_file_manager[output_info['type']] = file_path
            else:
                # Here's skipping initialization for saving to DB
                pass

    def add_item(self, item):
        self.buffer.append(item)

    def save(self):
        for save_type in self.save_file_manager:
            if save_type == EnumManager.CSV:
                self._save_csv()
            elif save_type == EnumManager.JSON:
                self._save_json()
            elif save_type == EnumManager.XML:
                self._save_xml()
            elif save_type == EnumManager.MONGO:
                self._save_mongo()
            elif save_type == EnumManager.SQL:
                self._save_sql()
            else:
                self.buffer.clear()
                raise Exception(f"The save method '{save_type}' is not supported.")

        self.buffer.clear()
        return self

    def _save_csv(self):
        keys = self.buffer[0].keys()
        with open(self.save_file_manager[EnumManager.CSV], 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.buffer)

    def _save_xml(self):
        pass

    def _save_json(self):
        pass

    def _save_mongo(self):
        pass

    def _save_sql(self):
        pass
