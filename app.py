from flask import Flask, redirect, render_template, request, flash, session
from flask_session import Session
import json
import os
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


def write_user(new_user):
    file_path = "data/user.json"
    
    # Check if the database file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            # Load existing data
            data = json.load(read_file)
            
            """ This line ensures that the json file is a dictionary first, 
            then if that dictionary has an element of "user", and finall
            if the "user" element is list
            Source for isinstance(): https://www.w3schools.com/python/ref_func_isinstance.asp"""
            
            if isinstance(data, dict) and "user" in data and isinstance(data["user"], list):
                users = data["user"]
            else:
                return "Error sending over data to the database"
    else:
        # If it doesn't exist, initialize with an empty list
        data = {"user": []}
        users = data["user"]

    # Append the new user to the list
    users.append(new_user)

    # Write the updated data back to the file
    with open(file_path, "w") as user_file:
        json.dump(data, user_file, indent=4)

    return "User added successfully!"


""" The weird line used below with the next() is called a generator expression which 
    loops through the read database that is users and checks if the database contains
    the requested username.
    source: https://www.geeksforgeeks.org/generator-expressions/
    
    next() function returns the next item in an iterable
    source: https://docs.python.org/3/library/functions.html#next"""

def check_username(username):
    users = read_user()
    for user in users:
        if user == username:
            return True
    return False
    
def check_password(input_password, username):
    users = read_user()
    for user in users:
        
        if user == username:
            user_password = (user["password"] == input_password)
            if user_password:
                return True
        return False
    return "Error finding password in database"


# @app.route("/")
# def index():
#     return render_template("homePage.html")

# @app.route("/homePage")
# def homePage():
#     redirect("")

@app.route("/login", methods=["POST", "GET"])
def login():
    # clear the previous session
    session.clear()
    # check if the username is provided, if not prompt the user to input it
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username:
            flash("Must Enter Username")
            return render_template("login.html")
        elif not password:
            flash("Must Entere Password")
            return render_template("login.html")
        
        user = check_username(username)
        if user == False:
            flash("Username does not exist!")
            return render_template("login.html")
        
        checked_password = check_password(password)
        if checked_password == False:
            flash("Wrong password!")
            return render_template("login.html")
        
        session["username"] = user["username"]
        return redirect("/")
    
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
@app.route("/register.html", methods=["POST", "GET"])
def register():
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        account_type = request.form.get("account_type")
        # idk if I should compare the password and the confirm password here or somewhere else
        
        checked_username = check_username(username)
        if checked_username == False:
            user_data = {
                "username": username,
                "password": password,
                "email": email,
                "account_type": account_type
                }
            write_user(user_data)
            session["username"] = user_data["username"]
            return redirect("/")
        
        return "Username already exists, choose a different username."
    
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

def rank_quiz(category):
    # establish a connection to the database
    # based on the argument passed to this function query the database
    # store the titles of the 
    return "To-do"

# # Redirecting user to the termsAndConditionsPage.html
# @app.route("/terms-and-conditions")
# def terms_and_conditions():
#     return render_template("termsAndConditionsPage.html")

# # redirecting user to the privacyPolicyPage.html file
# @app.route("/privacy-Policy")
# def privacy_policy():
#     return render_template("privacyPolicyPage.html")

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

@app.route("/homePage")
def homePage():
    return render_template("homePage.html")

@app.route("/createQuiz")
def createQuiz():
    return render_template("createQuiz.html")

@app.route("/quizList")
def quizList():
    return render_template("quizList.html")

@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html")

@app.route("/loginPage")
def loginPage():
    return render_template("login.html")

@app.route("/termsAndConditions")
def termsAndConditions():
    return render_template("termsAndConditions.html")

@app.route("/privacyPolicy")
def privacyPolicy():
    return render_template("privacyPolicy.html") 
    
if __name__ == "__main__":
    app.run(debug=True)