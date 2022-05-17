from random import randint, choice

from . import HEADERS, FILENAME

positions = ('Trainee', 'Junior', 'Middle', 'Senior', 'Lead')
profiles = ('Dev', 'DevOps', 'QA', 'PM')


def create_csv():
    with open(FILENAME, 'w') as fwriter:
        headers = list(HEADERS.keys())

        fwriter.write(','.join(headers[0]) + '\n')
        for i in range(250):
            fwriter.write(
                f'{randint(2500, 10000)},name_{i},surname_{i},{choice(positions)},{choice(profiles)}' + '\n'
            )

        fwriter.write(','.join(headers[1]) + '\n')
        for i in range(250):
            fwriter.write(
                f'{randint(1, 10)},description_{i}' + '\n'
            )

        fwriter.write(','.join(headers[2]) + '\n')
        for i in range(250):
            fwriter.write(
                f'{randint(1, 199)},comment_{i}' + '\n'
            )

        fwriter.write(','.join(headers[3]) + '\n')
        for i in range(250):
            fwriter.write(
                f'{randint(1, 199)},attachment_{i}' + '\n'
            )
