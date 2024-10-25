var form = document.getElementById('login');
form.addEventListener('submit',function(event){
    event.preventDefault();
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    let isValid = true;

    let emailRagex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    let passwordRagex = /^[A-Za-z0-9]+$/;

    if(!emailRagex.test(email)){
        displayErrorMessage("email", "please enter a valid email address");
        isValid = false;
        return;
    }
    if(!passwordRagex.test(password)){
        displayErrorMessage("password", "please enter a valid email address");
        isValid = false;
        return;
    }

    function displayErrorMessage(inputId, message){
    clearErrorMessage();
    let inputElement = document.getElementById(inputId);
    let errorElement = document.createElement("div");
    errorElement.className="error"
    errorElement.innerHTML = message;
    inputElement.parentElement.insertBefore(errorElement,inputElement.nextSibling);
    }
    function clearErrorMessage(){
        let errors = document.getElementsByClassName("error");
        while (errors[0]){
            errors[0].parentNode.removeChild(errors[0]);
        }
    }
    if(isValid){
        HTMLFormElement.prototype.submit.call(form)
    }









})