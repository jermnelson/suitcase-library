__author__ = "Jeremy Nelson"
__version__ = "0.0.1"

import os
import pathlib

from typing import Optional

import rdflib
import yaml

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from queries import BOOKS

app = FastAPI()
app.mount("/static", StaticFiles(directory="assets"), name="static")

branch = os.getenv("BRANCH")

templates = Jinja2Templates(directory="templates/")

def collection_graph():
    collections = rdflib.Graph()
    for path in pathlib.Path("40-49 Collections/").glob("**/*.ttl"):
        collections.parse(path, format='turtle')
    return collections

collections = collection_graph()

class ChatSession(BaseModel):
    question: str


@app.post("/chat/{person}")
async def chat(chat_session: ChatSession, person: str):
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

@app.get("/browse/{collection}")
def collection(request: Request, collection: str):
    context = { 'request': request, 'branch': branch}
    match collection:
        case "books":
            books = {}
            for row in collections.query(BOOKS):
                uri = str(row[0])
                if str(row[0]) in books:
                    books[uri]['authors'].append(str(row[2]))
                else:
                    books[uri] = {'title': str(row[1]), 'authors': [str(row[2])]}
            context['books'] = books
            return templates.TemplateResponse('books.html', context=context)
        case "music":
            return templates.TemplateResponse('music.html', context=context)
        case "video":
            return templates.TemplateResponse('video.html', context=context)
        case _:
            return templates.TemplateResponse('collections.html', context=context)


@app.get("/faq")
def frequently_asked_questions(request: Request):
    return templates.TemplateResponse('faq.html', context={ 'request': request, 'branch': branch})

@app.get('/staff')
def staff_home(request: Request):
    context = { 'request': request, 'branch': branch}
    return templates.TemplateResponse('staff.html', context=context)
    

@app.get("/staff/{member}")
def staff(request: Request, member: str):
    context = { 'request': request, 'branch': branch}
    staff_directory = pathlib.Path("20-29 Staff")
    match member:
        case "librarian":
            eliza_path = staff_directory / "20.01 Librarian/eliza-james.yaml"
            context["character"] = yaml.full_load(eliza_path.read_text())
            return templates.TemplateResponse('eliza-james.html', context=context)
        case 'cataloger':
            dun_path = staff_directory / "21.01 Cataloger/dun.yaml"
            context['character'] = yaml.full_load(dun_path.read_text())
            return templates.TemplateResponse('dun.html', context=context)
        case 'clerk':
            jerms_path = staff_directory / "22.01 Circulation and Maintenance/jerms-a-ally.yaml"
            context['character'] = yaml.full_load(jerms_path.read_text())
            return templates.TemplateResponse('jerms-a-ally.html', context=context)
        case 'systems':
            kumo_path = staff_directory / "23.01 System Administration and Web Designer/kumo.yaml"
            context['character'] = yaml.full_load(kumo_path.read_text())
            return templates.TemplateResponse('kumo.html', context=context)
        case _:
            return templates.TemplateResponse('staff.html', context=context)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={ 'request': request, 'branch': branch})