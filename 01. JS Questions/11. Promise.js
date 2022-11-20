/**
 * An Object used for asynchronous operations with a state of "pending", "fulfilled", "rejected".
 */
const promise = new Promise((res, rej) => res(2));

/**
 * resolve(value) : fulfills the promise and set its value.
 * reject(error) : reject the promise and set ans error message.
 */

console.log(promise); // Promise { 2 }

/**
 * then(fulfilledFnc, rejectedFnc) : call fulfilledFnc is the promise fulfilled, else call rejectedFnc.
 *                                   return new fulfilled Promise with the return value.
 * catch(rejectedFnc) : call rejectedFnc is promise rejected. return new fulfilled Promise with the return value.
 * finally(cb) : call cb whenever the promise settled.
 */

promise
  .then((val) => val * 5)
  .then((val) => val - 5)
  .then((val) => {
    console.log(val);
    // throw new Error('Error thrown!');
  })
  .catch((err) => console.log(err))
  .finally(() => {
    console.log('Done!');
  });

/**
 * Promise.all() : returns a single Promise. This returned promise fulfills when all of the input's promises fulfill. It rejects when any of the input's promises rejects, with this first rejection reason.
 */

const p1 = new Promise((res) => res(1));
const p2 = new Promise((res) => res(2));
const p3 = new Promise((res, rej) => rej(3));
const p4 = new Promise((res) => res(4));

const singlePromise = Promise.all([p1, p2, p3, p4]);
singlePromise.then((val) => console.log(val)); // [ 1, 2, 3, 4 ]

/**
 * Promise.allSettled() : This returned promise fulfills when all of the input's promises settle.
 */

const singlePromiseSettled = Promise.allSettled([p1, p2, p3, p4]);
singlePromiseSettled.then((val) => console.log(val));
/**
 [
  { status: 'fulfilled', value: 1 },
  { status: 'fulfilled', value: 2 },
  { status: 'rejected', reason: 3 },
  { status: 'fulfilled', value: 4 }
]
 */

/**
 * Promise.race() : This returned promise settles with the eventual state of the first promise that settles.
 */
