document.getElementById("signupForm").addEventListener("submit", async function(event) {  
    event.preventDefault(); // Предотвращаем отправку формы  

    const email = document.getElementById("email").value;  
    const fullname = document.getElementById("fullname").value;  
    const password = document.getElementById("password").value;  

    const response = await fetch("http://127.0.0.1:8000/user/singup", {  
        method: "POST",  
        headers: {  
            "Content-Type": "application/json"  
        },  
        body: JSON.stringify({ email, fullname, password })  
    });  

    const result = await response.json();  
    console.log(result); // Выводим ответ сервера в консоль  
    if (response.ok) {  
        alert("User created successfully!");  
    } else {  
        alert("Error: " + result.detail);  
    }  
});  


const btn_login = document.querySelector("#btn_login");  

btn_login.addEventListener('click', async function() {  
    console.log('click');
    // Перенаправление на страницу логина  
    window.location.href = "login.html"; // Замените "login.html" на ваш URL  
}); 


const btn_singup = document.querySelector("#btn_singup");

btn_singup.addEventListener('click', async function() {  
    console.log('click');
    // Перенаправление на страницу логина  
    window.location.href = "index.html"; // Замените "login.html" на ваш URL  
}); 