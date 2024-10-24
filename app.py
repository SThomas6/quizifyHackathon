from flask import Flask, redirect, render_template, request, flash, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
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
quizDatabase = "data/quiz.json"
userDatabase = "data/user.json"

quizDatabaseVar = "quiz"
userDatabaseVar = "user"

# For reading data from the database (experimental)
def read_quiz():
    try:
        with open(quizDatabaseVar, 'r') as quiz_file:
            return json.load(quiz_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def read_user():
    try:
        with open(userDatabase, 'r') as user_file:
            return json.load(user_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# For writing data to the database (experimental)
def write_quiz(data):
    with open(quizDatabase, "w") as quiz_file:
        json.dump(data, quiz_file, indent=4)


def writeToDatabase(new_element, database_route, database):
    file_path = database_route
    
    # This line checks if the json file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            # Load existing data
            data = json.load(read_file)
            
            """ This line ensures that the json file is a dictionary first, 
            then if that dictionary has an element of the database (either user or quiz), 
            and finall it checks whether the element is list.
            Source for isinstance(): https://www.w3schools.com/python/ref_func_isinstance.asp"""
            
            if isinstance(data, dict) and database in data and isinstance(data[database], list):
                users = data["user"]
            else:
                return "Error sending over data to the database"
    else:
        # If the json file does not exist, it will create a new one
        data = {"user": []}
        users = data["user"]

    # This appends the new user to the list
    users.append(new_element)

    # The below line writes the updated data back to the file
    with open(file_path, "w") as user_file:
        json.dump(data, user_file, indent=4)

    return "User added successfully!"


""" The weird line used below with the next() is called a generator expression which 
    loops through the read database that is users and checks if the database contains
    the requested email.
    source: https://www.geeksforgeeks.org/generator-expressions/
    
    next() function returns the next item in an iterable
    source: https://docs.python.org/3/library/functions.html#next"""

def check_email(email):
    users = read_user().get("user", [])  # this line tries to read the "user" database and in the case it doen't exist it will create a new list
    email = email.lower()  # turning the email argument to lowercase letter

    for user in users:
        if user["email"].lower() == email:  # check if the the result of turning the stored email and the passed email have the same value
            return True
    return False
    
# def check_password(input_password, email):
#     users = read_user()
#     for user in users:
#         if user == email:
#             user_password = (user["password"] == input_password)
#             if user_password:
#                 return True
#     return False

def check_password(password, email):
    users = read_user().get("user", [])
    
    email = email.lower()  # turning the email argument to lowercase letter

    for user in users:
        if user["email"].lower() == email:  # check if the the result of turning the stored email and the passed email have the same value
            if user["password"] == password:
                return True
    return False

""" The server needs to receive t"""

# @app.route("/")
# def index():
#     return render_template("homePage.html")

# @app.route("/homePage")
# def homePage():
#     redirect("")

@app.route("/login", methods=["POST", "GET"])
def login():
    
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")  # Don't hash this here
        
        if not email:
            flash("Must Enter Email")
            return render_template("login.html")
        
        elif not password:
            flash("Must Enter Password")
            return render_template("login.html")
        
        user = check_email(email)
        if not user:
            flash("Email does not exist!")
            return render_template("login.html")
        
        else:
            # Use check_password_hash to compare input password and stored password hash
            if check_password(password, email) == True:
                session["email"] = email
                return redirect("/")
            else:
                flash("Wrong Password")
                return render_template("login.html")
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
@app.route("/register.html", methods=["POST", "GET"])
def register():
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        account_type = request.form.get("account_type")
        # idk if I should compare the password and the confirm password here or somewhere else
        
        checked_email = check_email(email)
        if checked_email == False:
            user_data = {
                "email": email,
                "password": password,
                "account_type": account_type
                }
            writeToDatabase(user_data, userDatabase, userDatabaseVar)
            session["email"] = user_data["email"]
            return redirect("/")
        
        return "email already exists, login instead."
    
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

@app.route("/create-quiz")
def create_quiz():
    return render_template('createQuiz.html')

#submit quiz function to collect the create quiz data
@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    #getting the data from the form and putting it into a variable
    quizTitle = request.form.get('quizTitleInput')
    quizDescription = request.form.get('quizDescriptionInput')
    selectedCategory = request.form.get('categoryInput')
    questionTitle = request.form.get('questionTitleInput')

    #Getting the answers from teh form and putting them into a variable
    questionAnswer1 = request.form.get('answer1Input')
    questionAnswer2 = request.form.get('answer2Input')
    questionAnswer3 = request.form.get('answer3Input')

    #Getting the value of the checkbox from the form and checking if the value is true or false
    correctAnswer1 = True if request.form.get('correctAnswer1') else False
    correctAnswer2 = True if request.form.get('correctAnswer2') else False
    correctAnswer3 = True if request.form.get('correctAnswer3') else False


    #printing the data to the console
    print(f"Quiz Title: {questionTitle}")
    print(f"Description: {quizDescription}")
    print(f"Category: {selectedCategory}")
    print(f"Question Title: {questionTitle}")

    #Getting the answers that have been submitted
    print(f"Question Answer 1: {questionAnswer1}")
    print(f"Question Answer 2: {questionAnswer2}")
    print(f"Question Answer 3: {questionAnswer3}")

    #Getting the boolean value of the checkbox to check which answer is correct
    print(f"Correct answer 1: {correctAnswer1}")
    print(f"Correct answer 2: {correctAnswer2}")
    print(f"Correct answer 3: {correctAnswer3}")

    # returning inputs
    return f"Quiz submitted! Title: {quizTitle}, Category: {selectedCategory}"
    
if __name__ == "__main__":
    app.run(debug=True)