from ht_7_1.src.db_connection_ import session
from ht_7_1.src.models_ import Group


def create_groups(groups: list):
    for gr_name in groups:
        group = Group(group_name=gr_name)
        session.add(group)
        session.commit()
    session.close()
