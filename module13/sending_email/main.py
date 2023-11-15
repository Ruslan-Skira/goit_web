import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

load_dotenv()

class EmailSchema(BaseModel):
	email: EmailStr

conf = ConnectionConfig(
	MAIL_USERNAME=os.environ['MAIL_USERNAME'],
	MAIL_PASSWORD=os.environ['MAIL_PASSWORD'],
	MAIL_FROM=os.environ['MAIL_FROM'],
	MAIL_PORT=465,
	MAIL_SERVER="smtp.meta.ua",
	MAIL_FROM_NAME="From future Python developers",
	MAIL_STARTTLS=False,
	MAIL_SSL_TLS=True,
	USE_CREDENTIALS=True,
	VALIDATE_CERTS=True,
	TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
	)
print(Path(__file__).parent / 'templates')
app=FastAPI()

@app.post("/send-email")
async def send_in_background(backgound_tasks: BackgroundTasks, body:EmailSchema):
	message = MessageSchema(
		subject="From Pythond devs",
		recipients=[body.email],
		template_body={"fullname": "Mark"},
		subtype=MessageType.html,
    )
	fm = FastMail(conf)
	backgound_tasks.add_task(fm.send_message, message, template_name="python_event.html")
	return {"message": "email has been sent"}

if __name__=="__main__":
	uvicorn.run("main:app", port=8000, reload=True)
