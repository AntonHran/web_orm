import os
import sys

from repository_ import get_table

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db_connection_ import session


def read_table(model: str, id_: int = None):
    table = get_table(model)
    if not id_:
        return session.query(table).all()
    return session.query(table).filter(table.id == id_).all()


def return_read_res(res, model):
    if model == "Group":
        for r in res:
            print(r.id, r.group_name)
    elif model == "Student":
        for r in res:
            print(
                r.id, r.first_name, r.last_name, r.email, r.phone, r.address, r.group_id
            )
    elif model == "Lector":
        for r in res:
            print(
                r.id,
                r.first_name,
                r.last_name,
                r.email,
                r.phone,
                r.address,
                r.start_work,
            )
    elif model == "Subject":
        for r in res:
            print(r.id, r.subject_name, r.lector_id)
    elif model == "Mark":
        for r in res:
            print(r.id, r.grade, r.lesson_date, r.student_id, r.subject_id)
