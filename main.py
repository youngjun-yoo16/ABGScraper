import csv
import shutil
import uvicorn
import instaloader
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
bot = instaloader.Instaloader()
nameStorage = "null"

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Endpoint for validate button.
@app.post("/")
async def validate_username(request: Request, username = Form()):
    if username != 'pfpDownload' and username != 'scrap':
        print(username)
        try:
            bot.download_profile(username, profile_pic_only = True)
            dirpath = Path(username) 
            if dirpath.exists() and dirpath.is_dir():
                shutil.rmtree(dirpath)
        except:
            return templates.TemplateResponse("flash.html", {"request": request})
        return templates.TemplateResponse("pfp.html", {"request": request})

#FastApi treats the parameter of the post method as that of flask's request.form[name] 
#In this case, operations is the same as request.form["operations"]
@app.post("/")
async def get_profile_picture(request: Request, username = Form(), operations = Form()):
    if operations == "pfpDownload":
        print("poop")
        return templates.TemplateResponse("pfp.html", {"request": request})
    #else:
    #    print(username)
    #    pass
    #    nameStorage = username
    #    get_post_info_csv("user_info", )
        
def get_post_info_csv(filename, username):
    '''Note: login required to get post details.'''
    bot.login(input("Input your username: "), input("Input your password: ") ) 
    with open(filename + '.csv', 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Post Caption", "Post Date", "Post URL", "Mentions in Caption", "Tagged Users"])
        posts = instaloader.Profile.from_username(bot.context, username).get_posts()
        for post in posts:
            location_match = ["san francisco", "california", "bay area"]
            major_match = ["computer science", "data science", "comp sci", "data sci"]
            if any(keyword in str(post.caption).lower() for keyword in location_match) and any (keyword in str(post.caption).lower() for keyword in major_match):
                print("Post date: " + str(post.date))
                print("Post profile: " + post.profile)
                print("Post caption: " + post.caption)
                posturl = "https://www.instagram.com/p/" + post.shortcode
                print("Post url: " + posturl)
                writer.writerow([post.caption, post.date, posturl, post.caption_mentions, post.tagged_users])
                print("\n\n")
                
@app.get("/pfp")
async def download_users_profile_picture(request: Request):
    bot.download_profile(nameStorage, profile_pic_only = True)
    return templates.TemplateResponse("pfp.html", {"request": request})

@app.get("/flash")
async def display_flash_page(request: Request):
    return templates.TemplateResponse("flash.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)