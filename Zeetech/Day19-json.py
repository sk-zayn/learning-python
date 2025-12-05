import json
from pathlib import Path
import sqlite3
student = [{ "name": "Alice", "age": 21, "course": "Math"},
          { "name": "Bob", "age": 22, "course": "English" }]
data = json.dumps(student)
Path("student.json").write_text(data)  #using path will print output as a string
print(type(data))

json_data = json.loads(data)    #using loads will convert string back to list of dictionary
print(json_data)
for i in json_data:
    print(i)
print(type(json_data))

data = Path("student.json").read_text()
json_data = json.loads(data)
conn = sqlite3.connect('db.sqlite3')
query = 'insert into student values(?,?,?)'
for i in json_data:
    conn.execute(query, tuple(i.values()))

