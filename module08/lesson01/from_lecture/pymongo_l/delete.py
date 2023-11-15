

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://skiraruslan:TxwLfGrycmf1W4l9@cluster0.jtffrws.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
db = client.school

result = db.students.find_one({"name": "Lama"})

db.students.delete_one({"name": "Lama"})

result = db.students.find_one({"name": "Lama"})
print(result)