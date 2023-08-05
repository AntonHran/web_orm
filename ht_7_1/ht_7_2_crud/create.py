import os
import sys

# from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db_connection_ import session
from src.models_ import Group, Student, Lector, Subject, Mark, Base


def create_group(group: str):
    group = Group(group_name=group)
    session.add(group)
    session.commit()
    session.close()


def create_student(first_name, last_name, email, phone, address, group_id):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        address=address,
        group_id=group_id,
    )
    session.add(student)
    session.commit()
    session.close()


def create_lector(first_name, last_name, email, phone, address, start_work):
    lector = Lector(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        address=address,
        start_work=start_work,
    )
    session.add(lector)
    session.commit()
    session.close()


def create_subject(subject_name, lector_id):
    subject = Subject(
        subject_name=subject_name,
        lector_id=lector_id,
    )
    session.add(subject)
    session.commit()
    session.close()


def create_mark(grade, lesson_date, student_id, subject_id):
    mark = Mark(
        grade=grade,
        lesson_date=lesson_date,
        student_id=student_id,
        subject_id=subject_id,
    )
    session.add(mark)
    session.commit()
    session.close()
