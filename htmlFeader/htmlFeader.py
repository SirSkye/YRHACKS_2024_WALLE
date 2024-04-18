from fastapi import FastAPI, Request, Depends, HTTPException, status, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from pydantic_models import *
# from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from typing import Annotated


client = FastAPI(debug=True)
#router=APIRouter()
# client.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
#client.include_router(router)

SECRET_KEY = "aba1f4e7fac9ac0b03d6d5b49d0ad592dd09abddd7f2330d4905f65f6a823092"
ALGORITHM = "HS256" #Hashing
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#client.run(degbug=True)


@client.get("/login",tags=["login"])
async def login(request:Request):
    context={"request":request}
    return templates.testLogin(request=context,name="testLogin.html")
    #return """<h3 onclick="myFunction(this, 'red')">Click me to change my color.</h3>


@client.get("/home/", response_class=HTMLResponse)
@client.get("/", response_class=HTMLResponse)
async def give_home_html(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=context, name="home.html")

# @client.get("/test/", response_class=HTMLResponse)
# async def give_test_htmp(request: Request):
#     context = {"request": request}
#     return templates.TemplateResponse(request=context, name="test.html")
