//Файл jsscript.js
// console.log('Helloworld!');

//Checking of Phone number field
function checkPhone() {
    var phone = document.getElementById("phone").value;
    //  var regex = /^\d{3}-(\d{3})-\d{3}$/;
    //   var regex = /^\+7?([0-9]{3})\)?[ ]?([0-9]{3})[ ]?([0-9]{2})[-]?([0-9]{2})$/;
    var regex = /^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$/;

    if (regex.test(phone)) { // if testing of first is true
        document.getElementById("phone_Check").style.color = "green";
        document.getElementById("phone").style.borderColor = "green";
        // document.getElementById("phone").style.color = "green";
        document.getElementById("phone_Check").innerHTML = "Телефон введен";
        return true;
    }
    else {// if it's not
        document.getElementById("phone_Check").style.color = "red";
        document.getElementById("phone").style.borderColor = "red";
        // alert('Введите номер телефона в формате +7(000)-000-00-00');
        // document.getElementById("phone").style.color = "red";
        document.getElementById("phone_Check").innerHTML = "Введите тел. в формате +7(000)-000-00-00!";
        return false;
    }
}

//Checking of name field
function checkName() {
    var name = document.getElementById("name").value;
    var regex = /[a-zA-Zа-яА-Я]/;

    if (regex.test(name)) { // if testing of first is true
        document.getElementById("name_Check").style.color = "green";
        document.getElementById("name").style.borderColor = "green";
        document.getElementById("name_Check").innerHTML = "Имя введено";
        //Upper case first symbols of name
        document.getElementById("name").style.textTransform = "capitalize";
        return true;
    }
    else {// if it's not
        document.getElementById("name_Check").style.color = "red";
        document.getElementById("name").style.borderColor = "red";
        document.getElementById("name_Check").innerHTML = "Введите ваше имя!";
        return false;
    }
}

//Checking of email field
function checkEmail() {
    var email = document.getElementById("email").value;
    var regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (regex.test(email)) { // if testing of first is true
        document.getElementById("email_Check").style.color = "green";
        document.getElementById("email").style.borderColor = "green";
        document.getElementById("email_Check").innerHTML = "Email введён";
        return true;
    }
    else {// if it's not
        document.getElementById("email_Check").style.color = "red";
        document.getElementById("email").style.borderColor = "red";
        document.getElementById("email_Check").innerHTML = "Введите email корректно!";
        return false;
    }
}

//Button press
function outputData() {
    checkPhone();
    checkEmail();
    checkName();
    alert('Возможно ваше сообщение отправлено');
    let containerElement = document.querySelector('.Form');
    containerElement.style.backgroundColor = "green";
}
