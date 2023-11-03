const resultElement = document.getElementById("result");
const clearBtn = document.getElementById("clear-button");
const deleteBtn = document.getElementById("delete-button");
const divideBtn = document.getElementById("divide-button");
const multiplyBtn = document.getElementById("multiply-button");
const subtractBtn = document.getElementById("subtract-button");
const addBtn = document.getElementById("add-button");
const decimalBtn = document.getElementById("decimal-button");
const numberBtns = document.querySelectorAll(".number");
const equalBtn = document.getElementById("equal-button");
 
let result = "";
let operation = "";
let previousOperand = 0;
const appendNumber = (number) => {
    result += number;

}
numberBtns.foreach(button => {
    button.addEventListener('click',()=>{
        appendNumber(button.innerText);
    });
});