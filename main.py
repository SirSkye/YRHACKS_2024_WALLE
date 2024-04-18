from fastapi import FastAPI, Request, Depends, HTTPException, status, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from typing import Annotated


client = FastAPI(debug=True)
templates = Jinja2Templates(directory="templates")



@client.get("/login")
async def login(request:Request):
    context={"request":request}
    return templates.TemplateResponse(request=context,name="testLogin.html")
    #return """<h3 onclick="myFunction(this, 'red')">Click me to change my color.</h3>


@client.get("/home/", response_class=HTMLResponse)
@client.get("/", response_class=HTMLResponse)
async def give_home_html(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=context, name="home.html")

@client.get("/test/", response_class=HTMLResponse)
async def give_test_htmp(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=context, name="test.html")

@client.get("/loggedIn")
async def give_logginIn(request: Request):
    context = {"request", request}
    return templates.TemplateResponse()