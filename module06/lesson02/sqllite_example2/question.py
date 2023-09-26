import hashlib

import sqlite3


def md5sum(t):
    return hashlib.md5(t).hexdigest()
con = sqlite3.connect("salary.db")
con.create_function("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
    print(row)