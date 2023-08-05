from random import randint

from faker import Faker

from ht_7_1.src.db_connection_ import session
from ht_7_1.src.models_ import Student, Group


fake = Faker()


def create_students(num_students: int):
    groups = session.query(Group).all()
    for _ in range(num_students):
        student = Student(first_name=fake.first_name(),
                          last_name=fake.last_name(),
                          email=fake.ascii_free_email(),
                          phone=fake.phone_number(),
                          address=fake.address(),
                          group_id=randint(1, len(list(groups))))
        session.add(student)
        session.commit()
    session.close()
