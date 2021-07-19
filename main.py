import os
from dataclasses import asdict

import yaml

from models import UnifiedConvertor, OutputManager, InputManger
from utils import init_bank, ParseARGS


def main():
    ParseARGS.init()

    with open(ParseARGS.TEMPLATE_PATH, "r") as stream:
        template = yaml.load(stream.read(), Loader=yaml.FullLoader)

    output_manager = OutputManager(template['output_info'])

    for bank_info in template['files_info']:
        bank_config = init_bank(bank_info)
        converter = UnifiedConvertor(bank_config)

        for path in bank_config.files_path:
            reader = InputManger(path).get_reader()

            for item in reader:
                unified_data = converter.convert(item)
                output_manager.add_item(asdict(unified_data))

    output_manager.save()


if __name__ == "__main__":
    # For local testing
    os.environ['TEMPLATE_PATH'] = "template.yml"
    main()
