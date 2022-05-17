from . import HEADERS, FILENAME


class CSVReader:
    _instance = None
    data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def parse_file(cls):
        parsed_data = {k: [] for k in HEADERS.values()}
        current_header = None
        key = None
        for line in open(FILENAME, 'r'):
            line = tuple(line.strip().split(','))

            if HEADERS.get(line):
                key = HEADERS[line]
                current_header = line
                continue

            parsed_data[key].append(
                {k: v for k, v in zip(current_header, line)})
        return parsed_data

    @classmethod
    def read_csv(cls, key):
        assert key in HEADERS.values()
        if not cls.data:
            cls.data = cls.parse_file()
        return cls.data[key]
