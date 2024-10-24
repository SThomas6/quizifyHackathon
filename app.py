from flask import Flask, request, jsonify, render_template, request, redirect


app=Flask (__name__)
@app.route("/create_account",methods=['POST','GET'])
def create_account():
    if request.method =='GET':




        return render_template("createAccount.html")

    if request.method =='POST':

        data = request.form


        form_data = data.to_dict()
        print(form_data)

        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        phone=request.form.get('phone')

        print(name, email, password, phone)

    return "form submitted successfully"


if __name__ == '__main__':
    app.run(debug=True)



