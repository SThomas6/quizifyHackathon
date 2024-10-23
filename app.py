from flask import Flask, request, render_template, request, redirect

app=Flask (__name__)
@app.route("/login_page", methods=['POST','GET'])    
def login_page():
    if request.method =='GET':



        return render_template("LogIn.html")

    if request.method =='POST':
        data = request.form

        form_data = data.to_dict()
        print(form_data)

        email=request.form.get('email')
        password=request.form.get('password')

        print(email, password)
    
    return "you have successfull loged in"


if __name__ == '__main__':
    app.run(debug=True)
