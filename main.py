__author__ = "Jeremy Nelson"
__version__ = "0.0.1"


import pathlib

from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="assets"), name="static")

templates = Jinja2Templates(directory="templates/")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse('index.html', context={ 'request': request})