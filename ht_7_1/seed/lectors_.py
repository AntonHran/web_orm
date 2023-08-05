from faker import Faker

from ht_7_1.src.db_connection_ import session
from ht_7_1.src.models_ import Lector


fake = Faker()


def create_lectors(num_lectors: int):
    for _ in range(num_lectors):
        lector = Lector(first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        email=fake.ascii_free_email(),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        start_work=fake.date_between(start_date='-10y'))
        session.add(lector)
        session.commit()
    session.close()
