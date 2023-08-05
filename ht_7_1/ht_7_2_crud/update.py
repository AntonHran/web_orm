import os
import sys

# from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db_connection_ import session
from src.models_ import Group, Student, Lector, Subject, Mark, Base


def update_group(id_, group_name):
    group = session.query(Group).filter(Group.id == id_)
    if group:
        group.update({"group_name": group_name})
        session.commit()
    session.close()
    return group.first()


def update_student(id_, first_name, last_name, email, phone_number, address, group_id):
    student = session.query(Student).filter(Student.id == id_)
    if student:
        student.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone_number,
                "address": address,
                "group_id": group_id,
            }
        )
        session.commit()
    session.close()
    return student.first()


def update_lector(id_, first_name, last_name, email, phone_number, address, start_work):
    lector = session.query(Lector).filter(Lector.id == id_)
    if lector:
        lector.update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone": phone_number,
                "address": address,
                "start_work": start_work,
            }
        )
        session.commit()
    session.close()
    return lector.first()


def update_subject(id_, subject_name, lector_id):
    subject = session.query(Subject).filter(Subject.id == id_)
    if subject:
        subject.update({"subject_id": subject_name, "lector_id": lector_id})
        session.commit()
    session.close()
    return subject.first()


def update_mark(id_, grade, lesson_date, student_id, subject_id):
    mark = session.query(Mark).filter(Mark.id == id_)
    if mark:
        mark.update(
            {
                "grade": grade,
                "lesson_date": lesson_date,
                "student_id": student_id,
                "subject_id": subject_id,
            }
        )
        session.commit()
    session.close()
    return mark.first()


def return_updated_raw(model, res):
    if model == "Group":
        print(res.id, res.group_name)
    elif model == "Student":
        print(res.id, res.first_name, res.last_name, res.email, res.phone, res.address, res.group_id)
    elif model == "Lector":
        print(res.id,
              res.first_name,
              res.last_name,
              res.email,
              res.phone,
              res.address,
              res.start_work, )
    elif model == "Subject":
        print(res.id, res.subject_name, res.lector_id)
    elif model == "Mark":
        print(res.id, res.grade, res.lesson_date, res.student_id, res.subject_id)


def check_updated_row(model, updated_row):
    if updated_row:
        return_updated_raw(model, updated_row)
    else:
        print("Not found")
