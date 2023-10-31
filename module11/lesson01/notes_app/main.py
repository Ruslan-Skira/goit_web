from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    title: str
    description: str
    done: bool


@app.get("/api/healthchecker")
def root():
    return {"message": "Hello future python developers"}


"""CRUD notes"""


@app.get("/notes")
async def read_notes(skip: int = 0, limit: int = Query(default=10, le=3500, ge=3)):
    return {"message": f"Return all notes: skip {skip}, limit: {limit} "}


@app.post("/notes")
async def read_notes(note: Note):
    return {"title": note.title, "description": note.description, "status": note.done}


@app.get("/notes/new")
async def read_note():
    return {"message": "Just creating new notes"}


@app.get("/notes/{note_id}")
async def read_note(
    note_id: int = Path(description="the id of the note to get", gt=0, le=10)
):
    return {"note": note_id}
