import uvicorn
from fastapi import FastAPI

from src.routes import notes, tags, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
