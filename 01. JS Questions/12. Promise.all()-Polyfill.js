/**
 * The Promise.all() accepts an array of promises and returns a promise
that resolves when all of the promises in the array are fulfilled or when
the iterable contains no promises. It rejects with the reason of the first
promise that reject
 */

const myPromiseAll = function (tasks) {
  const results = new Array(tasks.length);
  let completedTasks = 0;

  return new Promise((resolve, reject) => {
    tasks.forEach((promise, index) => {
      promise
        .then((val) => {
          results[index] = val;
          completedTasks += 1;

          if (tasks.length === completedTasks) {
            resolve(results);
          }
        })
        .catch((error) => {
          reject(error);
        });
    });
  });
};

// Test case
function task(time) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      resolve(time);
    }, time);
  });
}

const taskList = [task(1000), task(5000), task(3000)];

//run promise.all
myPromiseAll(taskList)
  .then((results) => {
    console.log('got results', results);
  })
  .catch(console.error);
