
class NoteModel(BaseModel):
    name: str
    description: str
    done: bool


class ResponseNoteModel(BaseModel):
    done: bool
    id: int = Field(default=1, ge=1)
    name: str
    description: str