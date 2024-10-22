document.getElementById('create_account').addEventListener('submit',function(event) {
    event.preventDefault();
    var name = document.getElementById('name').Value;
    var email = document.getElementById('email').Value;
    var password = document.getElementById('password').value;
    var phone = document.getElementById('phone').value;

    let isValid = true;

    let nameRegex = /^[a-zA-Z\s]+$/;
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    let passwordRegex = /^[A-Za-z0-9]+$/;
    let phoneRegex = /^[0-9]{11}$/;



    if(!nameRegex.test(name)){
        displayErrorMessage("name","please enter a valid name(aplhabets only");
        isValid = false;
    }
    if(!emailRegex.test(email)){
        displayErrorMessage("email","please enter a valid email address");
        isValid = false;
    }
    if(!passwordRegex.test(password)){
        displayErrorMessage("password","please enter a vlid password (alphabets and numbers only)");
        isValid = false;
    }
    if(!phoneRegex.test(phone)){
        displayErrorMessage("phone","please enter a valid phone number 11 digit only" );
        isValid=true;
    }

    if(isValid){
        alert('form is valid submitting');
        this.submit();
    }
    function displayErrorMessage(inputId, message){
    clearErrorMessages();
    
    let inputElement = document.getElementById(inputId);
    let errorElement = document.createElement("section");
    errorElement.className = "error";
    errorElement.innerHTML = message;
    inputElement.parentElement.insertBefore(errorElement,inputElement.nextSibling);
    }
    function clearErrorMessages(){
        let errors = document.getElementsByClassName("error");
        while (errors[0]){
            errors[0].parentNode.removeChild(errors[0]);
        }
    }   
    




});