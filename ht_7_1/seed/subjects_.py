from random import randint

from ht_7_1.src.db_connection_ import session
from ht_7_1.src.models_ import Subject, Lector


def create_subjects(subjects: list):
    lectors = session.query(Lector).all()
    for subject_name in subjects:
        subject = Subject(subject_name=subject_name,
                          lector_id=randint(1, len(list(lectors))))
        session.add(subject)
        session.commit()
    session.close()
