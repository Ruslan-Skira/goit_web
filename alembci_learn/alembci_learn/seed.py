from connect_db import session
from models import Note, Record, Tag


if __name__ == "__main__":
    gr = Tag(name='groceries')
    food = Tag(name='food')

    note = Note(name="Mondey notes")

    note.tags = [gr, food]

    r1 = Record(description="Buy beer", note=note)
    r2 = Record(description="Buy milk", note=note)
    r3 = Record(description="Buy fish", note=note)

    session.add(note)
    session.commit()


