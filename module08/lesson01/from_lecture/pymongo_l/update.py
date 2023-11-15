from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://skiraruslan:TxwLfGrycmf1W4l9@cluster0.jtffrws.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)
db = client.school


db.students.update_one({"name": "Kiss"}, {"$set": {"age": 40}})
result = db.students.find_one({"name": "Kiss"}) # Get one record?
print(result)