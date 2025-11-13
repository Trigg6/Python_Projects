// script.js
// Demonstrating String and Math object functions in JavaScript

// --- STRING FUNCTIONS ---
const text = "Hello JavaScript!";
let stringOutput = "";

stringOutput += `<strong>Original String:</strong> ${text}<br><br>`;
stringOutput += `<strong>1. Length:</strong> ${text.length} <br>`;
stringOutput += `<strong>2. toUpperCase():</strong> ${text.toUpperCase()} <br>`;
stringOutput += `<strong>3. toLowerCase():</strong> ${text.toLowerCase()} <br>`;
stringOutput += `<strong>4. indexOf('Java'):</strong> ${text.indexOf('Java')} <br>`;
stringOutput += `<strong>5. slice(6, 10):</strong> ${text.slice(6, 10)} <br>`;
stringOutput += `<strong>6. replace('JavaScript', 'World'):</strong> ${text.replace('JavaScript', 'World')} <br>`;
stringOutput += `<strong>7. includes('Hello'):</strong> ${text.includes('Hello')} <br>`;
stringOutput += `<strong>8. charAt(4):</strong> ${text.charAt(4)} <br>`;
stringOutput += `<strong>9. split(' '):</strong> ${text.split(' ')} <br>`;

// Display the string results in the HTML element
document.getElementById("stringResults").innerHTML = stringOutput;


// --- MATH FUNCTIONS ---
const num = 7.56;
let mathOutput = "";

mathOutput += `<strong>Example Number:</strong> ${num}<br><br>`;
mathOutput += `<strong>1. Math.round(${num}):</strong> ${Math.round(num)} <br>`;
mathOutput += `<strong>2. Math.floor(${num}):</strong> ${Math.floor(num)} <br>`;
mathOutput += `<strong>3. Math.ceil(${num}):</strong> ${Math.ceil(num)} <br>`;
mathOutput += `<strong>4. Math.sqrt(25):</strong> ${Math.sqrt(25)} <br>`;
mathOutput += `<strong>5. Math.pow(3, 2):</strong> ${Math.pow(3, 2)} <br>`;
mathOutput += `<strong>6. Math.random():</strong> ${Math.random().toFixed(3)} <br>`;
mathOutput += `<strong>7. Math.max(3, 9, 2, 15):</strong> ${Math.max(3, 9, 2, 15)} <br>`;
mathOutput += `<strong>8. Math.min(3, 9, 2, 15):</strong> ${Math.min(3, 9, 2, 15)} <br>`;
mathOutput += `<strong>9. Math.abs(-10):</strong> ${Math.abs(-10)} <br>`;

// Display the math results in the HTML element
document.getElementById("mathResults").innerHTML = mathOutput;
