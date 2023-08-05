from datetime import date

from groups_ import create_groups
from subjects_ import create_subjects
from lectors_ import create_lectors
from students_ import create_students
from marks_ import create_marks_


groups: list[str] = ['MTO-08-2', 'IT-12-1', 'PTM-10-2']
subjects: list[str] = [
    'Maths',
    'Discrete maths',
    'Drawing',
    'Programing',
    'Probability theory',
    'DB theory',
    'English',
    'History of Ukraine'
]
NUMBER_STUDENTS: int = 50
NUMBER_LECTORS: int = 5

start_d: date = date(year=2022, month=9, day=1)
finish_d: date = date(year=2023, month=6, day=15)


def main():
    create_groups(groups)
    create_lectors(NUMBER_LECTORS)
    create_subjects(subjects)
    create_students(NUMBER_STUDENTS)
    create_marks_(start_d, finish_d)


if __name__ == '__main__':
    main()
