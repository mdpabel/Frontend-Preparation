/**
 *
 * JSON.stringify also has few surprising behaviors such as :
 * converting Date objects to ISO timestamp strings,
 * NaN and Infinity becoming null etc.
 */
const obj = {
  user: {
    role: 'admin',
  },
  isNull: null,
  isBool: true,
  isNum: 1,
  isStr: 'str',
  date: new Date(),
  isNan: NaN,
  isInfinity: Infinity,
  isUndefined: undefined,
};

const copy = JSON.parse(JSON.stringify(obj));

// const copy = obj

console.log(obj === copy);
console.log(obj, copy);

/**
-- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries

const entries = [
  ['foo', 'bar'],
  ['baz', 42]
]
Object.fromEntries(entries); // { foo: "bar", baz: 42 }

 */

function deepClone(obj) {
  if (typeof obj !== 'object' || obj === null) return obj;
  if (Array.isArray(obj)) {
    return obj.map((val) => deepClone(val));
  }

  return Object.fromEntries(
    Object.entries(value).map(([key, val]) => [key, deepClone(val)])
  );
}

const copy2 = deepClone(obj);

console.log(obj === copy);
console.log(obj, copy);

/**
 * using structuredClone method
 */

const copy3 = structuredClone(obj);

console.log(obj === copy);
console.log(obj, copy);
