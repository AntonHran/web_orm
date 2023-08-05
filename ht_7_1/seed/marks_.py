from random import randint
from datetime import date, timedelta

from ht_7_1.src.db_connection_ import session
from ht_7_1.src.models_ import Subject, Student, Mark


def get_dates(start: date, end: date) -> list[date]:
    result: list = []
    current_date: date = start
    while current_date <= end:
        if current_date.weekday() < 5:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def create_grades(dates_list: list[date], subj_num: int, st_num: int) -> list[list[int]]:
    grades: list = []
    for day in dates_list:
        subject_per_day: int = randint(1, subj_num)
        students_per_day: list = [randint(1, st_num) for _ in range(6)]
        for student in students_per_day:
            grades.append([randint(1, 100), day, student, subject_per_day])
    return grades


def create_marks_old(start_date: date, finish_date: date):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    dates = get_dates(start_date, finish_date)
    grades = create_grades(dates_list=dates, subj_num=len(list(subjects)), st_num=len(list(students)))
    for grade in grades:
        mark = Mark(grade=grade[0],
                    lesson_date=grade[1],
                    student_id=grade[2],
                    subject_id=grade[3])
        session.add(mark)
        session.commit()
    session.close()


def create_marks_(start_date: date, finish_date: date):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    dates = get_dates(start_date, finish_date)
    for date_ in dates:
        subjects_per_date: list[int] = [randint(1, len(list(subjects))) for _ in range(randint(2, 5))]
        for subject in subjects_per_date:
            students_per_subject: list = [randint(1, len(list(students))) for _ in range(randint(2, 6))]
            for student in students_per_subject:
                mark = Mark(grade=randint(1, 100),
                            lesson_date=date_,
                            student_id=student,
                            subject_id=subject)
                session.add(mark)
            session.commit()
    session.close()
