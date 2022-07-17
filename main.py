import instaloader
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
bot = instaloader.Instaloader()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#FastApi treats the parameter of the post method as that of flask's request.form[name] 
#In this case, operations is the same as request.form["operations"]
@app.post("/")
async def get_username(operations: str = Form()):
    print(operations)
    

@app.get("/pfp")
async def download_users_profile_picture(username, request: Request):
    bot.download_profile(username, profile_pic_only = True)
    return templates.TemplateResponse("pfp.html", {"request": request})