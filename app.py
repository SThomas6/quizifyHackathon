from flask import Flask, redirect, render_template

# might need flask_session library and session module

app = Flask(__name__)

@app.route("/")
def index():
    return ("todo!")

@app.route("/login")
def login():
    # clear the previous session
    # check if the username is provided, if not prompt the user to input it
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
    # wi
    return "To-do"

""" Database Structure:
        - User registry:
            - Columns:
                - id - auto incrmented (Has to be unique)
                - username (Has to be unique)
                - password
                - status of account (user or moderator)
                - id of quizzes taken (taken from the Quizzes database)
                - scores and results for each quiz
        
        - Quizzes:
            - Columns:
                - id - autoincrement Unique
                - title 
                - description
                - category
                - difficulty
"""

if __name__ == "__main__":
    app.run(debug=True)