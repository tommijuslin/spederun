function showErrorMsg(message) {
    document.getElementById("error-message").innerHTML = message;
    setTimeout(function(){
        document.getElementById("error-message").innerHTML = '';
    }, 5000);
}

function showSuccessMsg(message) {
    document.getElementById("success-message").innerHTML = message;
    setTimeout(function(){
        document.getElementById("success-message").innerHTML = '';
    }, 5000);
}
