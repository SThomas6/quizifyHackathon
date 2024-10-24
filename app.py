<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, flash, session
=======
from flask import Flask, redirect, render_template, request, flash
>>>>>>> bc530dfd1ad7c5e70302d5a213774a4e23e6fd3f
from flask_session import Session
import json

# might need flask_session library and session module
app = Flask(__name__)

<<<<<<< HEAD

# Testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
@app.route("/test-nav")
def test_nav():
    return render_template("navBar.html")





=======
>>>>>>> bc530dfd1ad7c5e70302d5a213774a4e23e6fd3f
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

<<<<<<< HEAD
@app.route("/login", methods=["POST","GET"])
=======
@app.route("/login")
>>>>>>> bc530dfd1ad7c5e70302d5a213774a4e23e6fd3f
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
<<<<<<< HEAD
    return render_template("login.html")
=======
    return redirect("login.html")
>>>>>>> bc530dfd1ad7c5e70302d5a213774a4e23e6fd3f

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



