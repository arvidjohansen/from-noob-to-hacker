---

---



# JavaScript Syntax Cheatsheet

## 1. Variables
```javascript
var variableName = value;
let anotherVariable = value;
const constantVariable = value;
```

---

## 2. Data Types
```javascript
let number = 10;
let string = 'Hello, World!';
let boolean = true;
let array = [1, 2, 3];
let object = { key: 'value' };
```

---

## 3. Operators
```javascript
let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;
let remainder = a % b;
```

---

## 4. Conditional Statements
```javascript
if (condition) {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```

---

## 5. Loops
```javascript
for (let i = 0; i < 5; i++) {
  // code to be repeated
}

while (condition) {
  // code to be repeated as long as condition is true
}
```

---

## 6. Functions
```javascript
function functionName(parameter1, parameter2) {
  // code to be executed
  return result;
}

// Arrow function
const arrowFunction = (parameter) => {
  // code to be executed
  return result;
};
```

---

## 7. Objects and Methods
```javascript
let car = {
  brand: 'Toyota',
  model: 'Camry',
  start: function() {
    // code to start the car
  }
};
```

---

## 8. Arrays and Methods
```javascript
let fruits = ['apple', 'banana', 'orange'];

fruits.push('grape'); // adds an element to the end of the array
fruits.pop(); // removes the last element of the array
```

---

## 9. DOM Manipulation (Browser)
```javascript
document.getElementById('elementId').innerHTML = 'New content';
document.querySelector('.className').style.color = 'red';
```

---

## 10. Events
```javascript
document.getElementById('myButton').addEventListener('click', function() {
  // code to be executed when the button is clicked
});
```
