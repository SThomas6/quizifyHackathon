from flask import Flask, redirect, render_template, request, flash, session, url_for
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

def writeToDatabase(new_element, database_route, database):
    file_path = database_route
    
    # This line checks if the json file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            # Load existing data
            data = json.load(read_file)
            
            """ The below line ensures that the json file is a dictionary first, 
            then if that dictionary has an element of the database (either user or quiz), 
            and finally it checks whether the element is list.
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

def writeNewsLetter(email):
    # Specifies the file path
    file_path = "data/newsLetter.json"

    # Checks if the json file exists
    
    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            # Load existing data in the database
            data = json.load(read_file)
        
            # Checks if the json file is a dictionary and if email is an element and if email is a list 
            if isinstance(data, dict) and "email" in data and isinstance(data["email"], list):
                subs = data["email"]
            else:
                return "Error sending over data to the database!"
    else:
        # if the json file does not exist, it will create a new one
        data = {"email": []}
        subs = data["email"]
    
    # Append the data
    subs.append(email)
    
    try:
        # Store the data in the database
        with open(file_path, "w") as write_file:
            json.dump(data, write_file, indent=4)
    except Exception as error:
        print(f"Failure to write to file: {error}")
    
    return "New subscriber added successfully"

def check_email(email):
    users = read_user().get("user", [])  # this line tries to read the "user" database and in the case it doen't exist it will create a new list
    email = email.lower()  # turning the email argument to lowercase letter

    for user in users:
        if user["email"].lower() == email:  # check if the the result of turning the stored email and the passed email have the same value
            return True
    return False

def check_password(password, email):
    users = read_user().get("user", [])
    
    email = email.lower()  # turning the email argument to lowercase letter

    for user in users:
        if user["email"].lower() == email:  # check if the the result of turning the stored email and the passed email have the same value
            if user["password"] == password:
                return True
    return False

@app.route("/loginPage", methods=["POST", "GET"])
def login():
    
    session.clear()
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")  # Don't hash this here
        
        if not email:
            flash("Must Enter Email")
            return render_template("LogIn.html")
        
        elif not password:
            flash("Must Enter Password")
            return render_template("LogIn.html")
        
        user = check_email(email)
        if not user:
            flash("Email does not exist!")
            return render_template("LogIn.html")
        
        else:
            # Use check_password_hash to compare input password and stored password hash
            if check_password(password, email) == True:
                session["email"] = email
                return redirect(url_for("homePage"))
            else:
                flash("Wrong Password")
                return render_template("LogIn.html")
    return render_template("LogIn.html")


@app.route("/register", methods=["POST", "GET"])
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
            return redirect(url_for("homePage"))
        
        return "email already exists, login instead."
    
    return render_template("createAccount.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("homePage"))

"""def rank_quiz(category):
    # establish a connection to the database
    try:
        with open(quizDatabaseVar, 'r') as quiz_file:
            return json.load(quiz_file)
        
        quizzesList = []
        
        for quiz in database["quiz"].items():
            if quiz["category"].lower() == category.lower():
                quizzesList.append({
                    "Title": quiz["quizTitleInput"],
                    "Description": quiz["quizDescriptionInput"],
                    "Category": quiz["categoryInput"],
                    "Question": quiz["questionTitleInput"]
                })
                
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    # based on the argument passed to this function query the database
    
    # store the titles of the 
    return "To-do" """

# Subscribing news letters
@app.route("/subscribe", methods=["POST", "GET"])
def subscribe():
    if request.method == ["POST"]:
        email = request.form.get('email')
        consent = request.form.get('consent')
    
        if email and consent: # this means if an email is inputed and the consent checkbox is ticked
            # code to store the email in a database (probably a dedicated table for the news-letter)
            # for now let's show it in the console for debugging, but ideally you would flash a success message
            writeNewsLetter(email)
            if result:
                return redirect(url_for("homePage"))
        else:
            return print("Sorry, you must provide an email and agree to our privacy policy to subscribe.")
    else:
        return print("Couldn't submit to database.")
    
@app.route("/")
def index():
    return redirect(url_for("homePage"))

@app.route("/homePage", methods=["POST", "GET"])
def homePage():
    return render_template("homePage.html")

@app.route("/createQuiz")
def createQuiz():
    return render_template("createQuiz.html")

@app.route("/quizList")
def quizList():
    return render_template("quizListPage.html")

@app.route("/createAccount")
def createAccount():
    return redirect(url_for("register"))

@app.route("/loginPage")
def loginPage():
    return redirect(url_for("login"))

@app.route("/termsAndConditions")
def termsAndConditions():
    return render_template("termsAndConditionPage.html")

@app.route("/privacyPolicy")
def privacyPolicy():
    return render_template("privacyPolicy.html")

@app.route("/quizTaking")
def quizTaking():
    return render_template("quizTaking.html")

@app.route("/create-quiz")
def create_quiz():
    return render_template('createQuiz.html')


def saveQuiz(quiz_details):
    file_path = "data/quiz.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as read_file:
            data = json.load(read_file)

            if isinstance(data, dict) and "quiz" in data and isinstance(data["quiz"], list):
                quizzes = data["quiz"]
            else:
                return "Error sending over data to the quiz database"
    else:
        data = {"quiz": []}
        quizzes = data["quiz"]

    quizzes.append(quiz_details)

    with open(file_path, "w") as quiz_file:
        json.dump(data, quiz_file, indent=4)

    return "Quiz was added successfully!"


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

    #Getting the value of the checkbox from the form and checking if the value is true or false
    correctAnswer1 = True if request.form.get('correctAnswer1') else False


    quizData={
        "quizTitle": quizTitle,
        "quizDescription": quizDescription,
        "selectedCategory": selectedCategory,
        "questionTitle": questionTitle,
        "questionAnswer1": questionAnswer1,
        "correctAnswer1": correctAnswer1
        }

    saveQuiz(quizData)


    #printing the data to the console
    print(f"Quiz Title: {questionTitle}")
    print(f"Description: {quizDescription}")
    print(f"Category: {selectedCategory}")
    print(f"Question Title: {questionTitle}")

    #Getting the answers that have been submitted
    print(f"Question Answer 1: {questionAnswer1}")


    #Getting the boolean value of the checkbox to check which answer is correct
    print(f"Correct answer 1: {correctAnswer1}")


    # returning inputs
    return redirect(url_for("quizTaking"))

if __name__ == "__main__":
    app.run(debug=True)