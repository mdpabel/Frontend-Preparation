//#########################################################################//
// this refers to the 'object' that is executing the current function. //
//########################################################################//

/**
 * If the new keyword is used when calling the function, this inside the function is a brand new object.
 */

function Student() {
  console.log(this); // {}
  this.name = 'MD';
  console.log(this); // {name: "MD"}
}

new Student();

/**
 * If apply, call, or bind are used to call a function, this inside the function is the object that is passed in as the argument.
 */

function Student() {
  console.log(this); // {name: "Pabel"}
  this.name = 'MD'; // Updated the name property of obj
  console.log(this); // {name: "MD"}
}

const obj = {
  name: 'Pabel',
};

Student.call(obj);

/**
 * If a function is called as a method, such as obj.method() — this is the object that the function is a property of.
 */

const student = {
  name: 'MD',
  print: function () {
    console.log(this); // {name: "MD", print: ƒ}
  },
};

student.print();

/**
 * If a function is invoked as a free function invocation, meaning it was invoked without any of the conditions present above, this is the global object.
 *  In a browser, it is the window object.
 * If in strict mode ('use strict'), this will be undefined instead of the global object.
 */

function test() {
  console.log(this); // Window{}
}

test();

/**
 * If the function is an ES2015 arrow function, it ignores all the rules above and receives the this value of its surrounding scope at the time it is created.
 */
const arrowStudent = {
  name: 'MD',
  print: () => {
    console.log(this); // {}
  },
};
arrowStudent.print();
console.log(this); // {}

const numsObj = {
  nums: [1],
  print: function () {
    this.nums.forEach(() => {
      console.log(this); // {nums: Array[4], print: ƒ}
    });
  },
};

numsObj.print();

/**
 * Example
 */
const obj1 = {
  value: 'hi',
  print: function () {
    console.log(this);
  },
};
const obj2 = { value: 17 };

obj1.print.call(obj2); // {value: 17}
new obj1.print(); // -> {}
obj1.print(); //{value: "hi", print: ƒ}

const person = {
  name: 'person',
  print: function () {
    console.log('Person Inside function', this); // {name: "person", print: ƒ}
    setTimeout(() => {
      console.log('Person arrow func', this); // {name: "person", print: ƒ}
    }, 100);
    setTimeout(function () {
      console.log('Person Regular func', this); // Window{}
    }, 100);
  },
};
person.print();

const person2 = {
  name: 'person',
  print: () => {
    console.log('person2 Inside function', this); // {}
    setTimeout(() => {
      console.log('person2 arrow func', this); // {}
    }, 100);
    setTimeout(function () {
      console.log('person2 Regular func', this); // Window{}
    }, 100);
  },
};
person2.print();
