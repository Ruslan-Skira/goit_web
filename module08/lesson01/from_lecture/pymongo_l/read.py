from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://skiraruslan:TxwLfGrycmf1W4l9@cluster0.jtffrws.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)

db = client.school

result = db.students.find_one({"_id": ObjectId("651c59ed194f96daddcaa8de")})
print('ONE reccord', result)
# MANY
results = db.students.find({})

for el in results:
    print(el)