var signUpName = document.getElementById('signName');
var signUpEmail = document.getElementById('signEmail');
var signUpPassword = document.getElementById('signPassword');
var user = [];

if (localStorage.getItem('user') != null) {
    user = JSON.parse(localStorage.getItem('user'))
} else {
    user = [];
}


// function add() {
//     if (signUpName.value == '' || signUpEmail.value == '' || signUpPassword.value == '') {
//         document.getElementById('message').innerHTML = `<p class = 'text-center'>All inputs is required</p>`
//     } else {
//         var obj = {
//             name: signUpName.value,
//             email: signUpEmail.value,
//             password: signUpPassword.value
//         }
//         user.push(obj);
//         location.href = '../../Templet/sigup.html';
//         localStorage.setItem('user', JSON.stringify(user));
//     }
// }
function submitForm() {
    // Get the form element by its ID
    var form = document.getElementById("signupForm");

    // Submit the form
    form.submit();
    }