import os
from sqlite3 import connect, IntegrityError

db_name = os.environ.get("CRYPTID_SQLITE_DB", "cryptid.db")
conn = connect(db_name, check_same_thread=False)
curs = conn.cursor()