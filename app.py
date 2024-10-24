from flask import Flask, redirect, render_template, request, flash
from flask_session import Session
import json

# might need flask_session library and session module

app = Flask(__name__)

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

# This section is to keep track of who is signed in
# The below line makes sure that the session is not forever, it will last until the web-browser is closed.
# app.config["SESSION_PERMANENT"] = False

# This makes sure the the session is saved on the server's file system and not on memory (which is temporary storage)
# app.config["SESSION_TYPE"] = "filesystem"

# This passes the app to the session
# Session(app)

# (experimental)
# data_file = "data/data.json"

# For reading data from the database (experimental)
# def read_data():
#     try:
#         with open(data_file, 'r') as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# For writing data to the database (experimental)
# def write_data(data):
#     with open(data_file, "w") as file:
#         json.dump(data, file, indent=4)

@app.route("/")
def index():
    return render_template("homePage.html")

@app.route("/login")
def login():
    # clear the previous session
    # session.clear()
    
    # check if the username is provided, if not prompt the user to input it
    # if request.method == "POST":
    #     if not request.form.get("username"):
    #         return "Must Enter Username"
    # elif not request.form.get("password"):
    #     return "Must Entere Password"
    
    # check if the username exists in the database, if it doesn't alert the user
    # if username exists compare the password the user inputed to the one stored in the database with the check_password function
    # if they match then store the session and redirect to the home page
    return "To-do"

def check_password(username, password):
    # establish a connection to the databse
    # look for the username in the database
        # if found store the password in a variable
        # compare the value of that variable with the password that the user just submitted aka(password argument)
        # if they match return true, else return false
    return "To-do"

@app.route("/register")
def register():
    # clear the session
    # store the inputed username in a variable
    # establish a connection to the database
    # check if that username already exists in the database
        # if yes, alert the user that that username is taken
        # else store the inputed password in a variable and store both the password and the username in the database
    # update the session
    # redirect to the home page
    return "To-do"

@app.route("/logout")
def logout():
    # clear the session
    # redirect to the home page
    return "To-do"

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

""" Database Structure:
        - User registry:
            - Columns:
                - id - auto incrmented (Has to be unique) (Unique id does not exist in json, I think?! so probably doesn't apply)
                - username (Has to be unique)
                - password
                - status of account (user or moderator)
                - id of quizzes taken (taken from the Quizzes database)
                - scores and results for each quiz
        
        - Quizzes:
            - Columns:
                - id - autoincrement Unique (Unique id does not exist in json, I think?! so probably doesn't apply)
                - title 
                - description
                - category
                - difficulty
"""

# def time_limit():

# def 

if __name__ == "__main__":
    app.run(debug=True)




