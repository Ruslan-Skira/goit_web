import time
import pathlib
from fastapi import FastAPI, Path, Query, Depends, HTTPException, Request, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from database.db import get_db, Note
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool


class ResponseNoteModel(BaseModel):
    done: bool
    id: int = Field(default=1, ge=1)
    name: str
    description: str


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configuret correctly"
            )
        return {
            "message": "Hello future python developers your DB connected and configured OK!"
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error!!! connectin to db ")


# def hello(name: str)-> str:
#     return f'hello {name}'


@app.get("/notes")
async def read_notes(
    skip: int = 0,
    limit: int = Query(default=10, le=100, ge=10),
    db: Session = Depends(get_db),
) -> list[ResponseNoteModel]:
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes


@app.post("/notes")
async def create_note(note: NoteModel, db: Session = Depends(get_db)):
    new_note = Note(name=note.name, description=note.description, done=note.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@app.get("/notes/new")
async def read_note():
    return {"message": "Just creating new notes"}


@app.get("/notes/{note_id}")
async def read_note(
    note_id: int = Path(description="the id of the note to get", gt=0, le=10)
):
    return {"note": note_id}


@app.middleware("http")
async def process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File()):
    pathlib.Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"file_path": file_path}

favicon_path = "/static/favicon.ico"
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(favicon_path)