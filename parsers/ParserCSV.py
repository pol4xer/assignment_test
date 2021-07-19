import csv


class ParserCSV:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                yield row
