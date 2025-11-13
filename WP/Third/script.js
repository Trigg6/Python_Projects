function validateForm() {
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const errorMessage = document.getElementById("error-message");

    // Clear previous errors
    errorMessage.textContent = "";

    // Username validation
    if (username === "") {
        alert ("Username is required.");
        return false;
    }

    // Email validation (simple regex)
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
        alert  ("Please enter a valid email address.");
        return false;
    }

    // Password validation
    if (password.length < 6) {
        alert ("Password must be at least 6 characters long.");
        return false;
    }

    // Confirm password validation
    if (password !== confirmPassword) {
        alert ("Passwords do not match.");
        return false;
    }

    alert("Registration successful!");
    return true;
}
