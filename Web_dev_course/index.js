// COUNTER PROGRAM
const decreaseBtn = document.getElementById("decreaseBtn");
const resetBtn = document.getElementById("resetBtn");
const increaseBtn = document.getElementById("increaseBtn");
const countLabel = document.getElementById("countLabel");

let count = 0;

increaseBtn.onclick = function(){
    count ++;
    countLabel.textContent = count;
}
decreaseBtn.onclick = function(){
    count --;
    countLabel.textContent = count;
}
resetBtn.onclick = function(){
    count = 0;
    countLabel.textContent = count;
}


// RANDOM PASSWORD GENERATOR
function generatePassword(length, includeLowercase, includeUppercase, 
    includeNumbers, includeSymbols){
        const lowercaseChars = "abcdefghijklmnopqrstuvxyz";
        const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVXYZ";
        const numberChars = "0123456789";
        const symbolChars = "!@#$%^&*()+_=-~`";

        let allowedChars = "";
        let password = "";

        allowedChars += includeLowercase ? lowercaseChars: "";
        allowedChars += includeUppercases ? uppercaseChars: "";
        allowedChars += includeNumbers ? numberChars: "";
        allowedChars += includeSymbols ? symbolChars: "";
        
        if (length <= 0){
            return `(password length must be at least 1)`;
        }
        if (allowedChars.length === 0){
            return `(At least 1 set of character needs to be selected)`;
        }
        for (let i = 0; i < length; i++){
            const randomIndex = Math.floor(Math.random() * allowedChars.length);
            password += allowedChars[randomIndex]
        }
        return '';

    }

const passwordLength = 12;
const includeLowercase = true;
const includeUppercase = true;
const includeNumbers = true;
const includeSymbols = true;

const password = generatePassword(passwordLength, includeLowercase, includeUppercase, includeNumbers, includeSymbols);


// Getter and Setter Method
class Person{
    constructor(firstName, lastName, age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age
    }
    set firstName (newFirstName){
        if (typeof newFirstName === "string" && newFirstName.length > 0){
            this._firstName = newFirstName;}
        else{
            console.error("First name must be a non-empty string.");
        }
    }
    set lastName(newLastName){
        if (typeof newLastName === "string" && newLastName.length > 0) {
            this._lastName = newLastName;
        }
        else{
            console.error("Last name must be a non-empty string.");
        }
    }
    set age(newAge){
        if (typeof newAge === "number" && newAge >= 0){
            this._age = newAge;
        }
        else{
            console.error("Age must be a non-negative number.");
        }
    }
    get firstName(){
        return this._firstName;
    }
    get lastName(){
        return this._lastName;
    }
    get fullname(){
        return this._firstName + " " + this._lastName;
    }
    get age(){
        return this._age;
    }
    
}
// JS
function Animal(name) {
    this.name = name;
}
Animal.prototype.speak = function () { // Animal.prototype call child of parent(Animal)
    console.log(`\ ${this.name} makes a sound.`);
};

// Child constructor function
function Dog(name) {
    Animal.call(this, name); // Inherit properties // like super() in Python
}

// Inherit methods from Animal
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Adding a new method to Dog
Dog.prototype.bark = function () {
    console.log(`\ ${this.name} barks: Woof!`);
};

// Creating an instance
const myDog = new Dog("Buddy");

// ES6 using extends

class one {
    constructor(name) {
        this.name = name
    }
    speaks() {
        return `my name is \${this.name}`
    }
}
class two extends one {
    constructor(name) {
        super(name)
    }
}
// Mixin
const one = {
    speak() {
        return `\ ${this.name} walks`
    }
}
const two = {
    walks() {
        return `\ ${this.name} walks`
    }
}
function Person(name) {
    this.name = name
}
Object.assign(Person.prototype, one, two)


// JS Events are actions or occurrences that happen in the browser. They ca be 
// triggered by various user interaction, or by the browser itself
// Event Types: MouseEvents: click, dbclick, mousemove, mouseover, mouseout
// Keyboard Events: keydown, keypress, keyup
// Form Events: submit, change, focus, blur
// window Events: load, resize, scroll

// onclick: Triggered when an element is clicked
// onmouseover: fired when the mouse pointer moves over an element
// onmouseout: mouse leave
// onkeydown: pressed down
// keyup: released
// onchange: input element change
// onload: page has finished loading
// onsubmit: form submitted
// onfocus: get focus
// onblue: element lose focus

btn.addEventListener("click", () => {alert("Button clicked using addEventListener!")});
// Event Propagation
// Query: chonj cau lenh
document.querySelector("div").addEventListener("click", () => {console.log("Div clicked")});

// Event Delegation
document.querySelector('ul').addEventListener('click', (e) => {
    if (e.target.tagName === "LI"){
        console.log(`Clicked on item: \${e.target.textContent}`);
    }
})

function calc(a, b, callback) {
    return callback(a, b);
}

function add(x, y) {
    return x + y;
}

function mul(x, y) {
    return x * y;
}
// Call api
function fetch(callback) {
    fetch("https://jsonplaceholder.typicode.com/todos/1")
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.error("Error:", error));
}

function handle(data) {
    console.log("Fetched Data:", data);
}

fetch(handle);
// Preventing Default Behavior: Certain elements

// Strict and error handling

// Avoiding accidental bugs and unsafe operations
"use strict";
function showValue() {
    x = 10;
}   // return x is not defined // using strict modes to catch common errors, prevent accidental globals, disallow deleting var, imporve performance
"use strict";
const obj = Object.freeze({ prop: 42 });
obj.prop = 50; // return x is not defined since freeze make let immutable, unchangeable
// 
try {
    const a = b
    console.log(a)
}
catch (error) {
    console.log('The error found here is', error)

}
finally {
    console.log('runs each and every time')
}
try {
    const a = 10;
    {
        if (a === 10) {
            throw Error("Error is caused due to throw statement");
        }
    }
    console.log(a);
} catch (error) {
    console.log("The error found here is", error);
} finally {
    console.log("runs each and every time");
}
// implement debugger between the code helps halts the browser's execution to inspect the code
async function f() {
    try {
        let response = await fetch('https://invalid.url');
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error.message);
    }
}

f();