#!/usr/bin/python
import MySQLdb
import json

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="vidoosh123",  # your password
                     db="test_db")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
client_id = "C0122"
data = []
response_data = {
    "client_id": client_id,
    "name": "name",
    "age": "age",
    "industry": "industry",
    "salary": "200",
    "city": "Tokyo",
}
# response_data = json.dumps(response_data)
data.append(client_id)
data.append(response_data)
tuple(data)
# data = json.dumps(data)
print(data)

cur.execute("INSERT INTO test_table (id, data) VALUES (%s, %s)", data)


# print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row)
db.commit()
db.close()