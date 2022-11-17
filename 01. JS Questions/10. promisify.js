function promisify(cb) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      function handleErrAndVal(error, value) {
        if (error) {
          reject(error);
        } else {
          resolve(value);
        }
      }
      cb.call(this, ...args, handleErrAndVal);
    });
  };
}

const add = (a, b, cb) => {
  const res = a + b;
  if (typeof res == 'number') {
    cb(null, res);
  } else {
    cb('the argument should be number', null);
  }
};

const promisifiedAdd = promisify(add);

promisifiedAdd(1, 2, (err, val) => {
  console.log(err, val);
});
