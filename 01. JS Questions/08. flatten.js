/**
[1, [2, [3, [4, [5]]]]]

copy = [1, [2, [3, [4, [5]]]]]
result = []

item = 1
copy = [[2, [3, [4, [5]]]]]
result = [1]

item = [2, [3, [4, [5]]]]
copy = [2, [3, [4, [5]]]]
result = [1]

item = [2]
copy = [[3, [4, [5]]]]
result = [1, 2]

item = [[3, [4, [5]]]]
copy = [3, [4, [5]]]
result = [1, 2]

item = [3]
copy = [[4, [5]]]
result = [1, 2, 3]

 */

/**
 * take out an item from the array
 * If the item is not an array, we put it into the res array.
 * If it is an array, we use a spread operator ... to get all the items out of it and put them back to the array.
 */

function flatten(array) {
  const result = [];
  const copy = array.slice();

  while (copy.length) {
    const item = copy.shift();
    if (Array.isArray(item)) {
      copy.unshift(...item);
    } else {
      result.push(item);
    }
  }
  return result;
}

console.log(flatten([1, [2, [3, [4, [5]]]]]));

/**
 *  Iterative Solution with Array.prototype.some
 */
function flatten(array) {
  while (array.some((arr) => Array.isArray(arr))) {
    array = [].concat(...array);
  }
  return array;
}

console.log(flatten([1, [2, [3, [4, [5]]]]]));
/**
 *  Recursive
 */
function flatten(arr, newArr) {
  for (const item of arr) {
    if (Array.isArray(item)) {
      flatten(item, newArr);
    } else {
      newArr.push(item);
    }
  }
}
const newArr = [];
flatten([1, [2, [3, [4, [5]]]]], newArr);
console.log(newArr);

/**
 * Recursive + reduce
 */
function flatten(arr) {
  return arr.reduce((acc, curr) => {
    if (Array.isArray(curr)) {
      return [...acc, ...flatten(curr)];
    } else {
      return [...acc, curr];
    }
  }, []);
}

console.log(flatten([1, [2, [3, [4, [5]]]]]));

/**
 * Array.prototype.flat
 */
function flatten(arr) {
  return arr.flat(Infinity);
}

console.log(flatten([1, [2, [3, [4, [5]]]]]));

/**
 * toString()
 */

function flatten(arr) {
  return arr.toString().split(',').map(Number);
}

console.log(flatten([1, [2, [3, [4, [5]]]]]));

/**
 * In place
 */

function flatten(array) {
  for (let i = 0; i < array.length; ) {
    if (Array.isArray(array[i])) {
      array.splice(i, 1, ...array[i]);
    } else {
      i++;
    }
  }
  return array;
}
console.log(flatten([1, [2, [3, [4, [5]]]]]));
