__author__ = "Jeremy Nelson"
__version__ = "0.0.1"

import os
import pathlib

from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="assets"), name="static")

branch = os.getenv("BRANCH")

templates = Jinja2Templates(directory="templates/")

class ChatSession(BaseModel):
    question: str


@app.post("/chat/{person}")
async def chat(chat_session: ChatSession, person: str):
    print(chat_session)
    response = ""
    match person:
        case "librarian":
            import eliza
            eliza_james = eliza.Eliza()
            eliza_james.load("assets/txt/librarian.txt")
            branch_chat = pathlib.Path(f"assets/txt/{branch}.txt")
            if branch and branch_chat.exists():
                eliza_james.load(branch_chat.path)
            response = eliza_james.respond(chat_session.question)
            if response is None:
                response = "Thank-you for your question, my name is Eliza"
        case _:
            response = f"{person} unknown"
    return { "response": response }


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={ 'request': request, 'branch': branch})