from flask import Flask, request, render_template, request, redirect

app=Flask (__name__)
@app.route("/loginPage", methods=['POST','GET'])    
def loginPage():
    if request.method =='GET':



        return render_template("login.html")

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
