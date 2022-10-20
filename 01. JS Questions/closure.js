/**
 * Function bundled with its lexical environment is known as a closure.
 * Whenever function is returned, even if its vanished in execution context but still it remembers the reference it was pointing to.
 */
function outer() {
  let num = 3;
  function inner() {
    console.log(num); // Here num doesn't refer to the value, It's refers to the reference to num.
  }
  num = 100;
  return inner;
}

const inner = outer();
inner(); // 100
