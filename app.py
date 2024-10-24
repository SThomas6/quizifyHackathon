from flask import Flask, redirect, render_template, request, flash
from flask_session import Session
import json

# might need flask_session library and session module
app = Flask(__name__)

# This section is to keep track of who is signed in
# The below line makes sure that the session is not forever, it will last until the web-browser is closed.
app.config["SESSION_PERMANENT"] = False

# This makes sure the the session is saved on the server's file system and not on memory (which is temporary storage)
app.config["SESSION_TYPE"] = "filesystem"

# This passes the app to the session
Session(app)

# (experimental)
quiz = "data/quiz.json"
user = "data/user.json"

# For reading data from the database (experimental)
def read_quiz():
    try:
        with open(quiz, 'r') as quiz_file:
            return json.load(quiz_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def read_user():
    try:
        with open(user, 'r') as user_file:
            return json.load(user_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# For writing data to the database (experimental)
def write_quiz(data):
    with open(quiz, "w") as quiz_file:
        json.dump(data, quiz_file, indent=4)

def write_user(data):
    with open(user, "w") as user_file:
        json.dump(data, user_file, indent=4)

""" The weird line used below with the next() is called a generator expression which 
    loops through the read database that is users and checks if the database contains
    the requested username.
    source: https://www.geeksforgeeks.org/generator-expressions/
    
    next() function returns the next item in an iterable
    source: https://docs.python.org/3/library/functions.html#next"""

def check_username(username):
    users = read_user()
    user = next((u for u in users if u["username"] == username), None)
    if user == None:
        return False
    
def check_password(input_password, username):
    users = read_user()
    user = next((u for u in users if u["username"] == username), None)
    if user != None:
        user_password = (user["password"] == input_password)
        if user_password:
            return True
        return False
    return "Error finding password in database"


@app.route("/")
def index():
    return render_template("homePage.html")

@app.route("/login")
def login():
    # clear the previous session
    session.clear()
    # check if the username is provided, if not prompt the user to input it
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username:
            return "Must Enter Username"
        elif not password:
            return "Must Entere Password"
        
        user = check_username(username)
        if user == False:
            return "Username does not exist!"
        
        checked_password = check_password(password)
        if checked_password == False:
            return "Wrong password!"
        
        session["username"] = user["username"]
        return redirect("/")
    return redirect("login.html")

@app.route("/register")
def register():
    session.clear()
    
    if request.method == "Post":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        account_type = request.form.get("account_type")
        # idk if I should compare the password and the confirm password here or somewhere else
        
        checked_username = check_username(username)
        if checked_username == False:
            user = write_user()
            user.append({"username": username, "password": password, "email": email, "account_type": account_type})
            session["username"] = user["username"]
            return redirect("/")
        
        return "Username already exists, choose a different username."
    
    return redirect("regist.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

def rank_quiz(category):
    # establish a connection to the database
    # based on the argument passed to this function query the database
    # store the titles of the 
    return "To-do"

# Redirecting user to the termsAndConditionsPage.html
@app.route("/terms-and-conditions")
def terms_and_conditions():
    return render_template("termsAndConditionsPage.html")

# redirecting user to the privacyPolicyPage.html file
@app.route("/privacy-Policy")
def privacy_policy():
    return render_template("privacyPolicyPage.html")

# Subscribing news letters
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get('email')
    consent = request.form.get('consent')
    
    if email and consent: # this means if an email is inputed and the consent checkbox is ticked
        # code to store the email in a database (probably a dedicated table for the news-letter)
        # for now let's show it in the console for debugging, but ideally you would flash a success message
        return email
    else:
        return flash("Sorry, you must provide an email and agree to our privacy policy to subscribe.")
if __name__ == "__main__":
    app.run(debug=True)