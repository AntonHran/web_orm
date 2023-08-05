import os
import sys

from repository_ import get_table

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.db_connection_ import session


def delete_table_row(id_, model):
    table = get_table(model)
    res = session.query(table).filter(table.id == id_).delete()
    session.commit()
    session.close()
    return res
