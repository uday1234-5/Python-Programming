// <!-- Create an array of numbers, and write JavaScript code to do the following:
// - Find and display the sum of all the numbers in the array.
// - Find and display the largest number in the array.
// - Sort the array in ascending order and display the sorted result. -->
// Create an array of numbers
const numbers = [8, 2, 10, 5, 14, 1, 7, 12];

// Find and display the sum of all the numbers in the array
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log("Sum of all numbers:", sum);

// Find and display the largest number in the array
const largestNumber = Math.max(...numbers);
console.log("Largest number:", largestNumber);

// Sort the array in ascending order and display the sorted result
const sortedArray = numbers.slice().sort((a, b) => a - b);
console.log("Sorted array in ascending order:", sortedArray);