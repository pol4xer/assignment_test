import argparse
import os

from models import Bank


def init_bank(bank_info: dict):
    bank = Bank(**bank_info)
    return bank


class ParseARGS:
    TEMPLATE_PATH = None
    error_text = "The following arguments are required: -t/--template or TEMPLATE_PATH environment variable"

    @staticmethod
    def init():
        my_parser = argparse.ArgumentParser()
        my_parser.add_argument('-t', '--template', default=os.environ.get("TEMPLATE_PATH"))
        args = my_parser.parse_args()

        assert args.template is not None, AssertionError(ParseARGS.error_text)

        ParseARGS.TEMPLATE_PATH = args.template
