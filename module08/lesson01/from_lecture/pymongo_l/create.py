from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://skiraruslan:TxwLfGrycmf1W4l9@cluster0.jtffrws.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)

db = client.school  # create db name

result_one = db.students.insert_one(
    {
        "name": "Kiss",
        "age": 4,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.students.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)


