function curry(cb) {
  const curriedCb = function (...args) {
    if (args.length === 0) return cb();
    return (...othersArg) => {
      if (othersArg.length === 0) cb(args);
      return curriedCb(...args, ...othersArg);
    };
  };
  return curriedCb;
}

curry(cb)(2)(3)(4)(5)(6)();

function cb(args) {
  let sum = 0;
  for (const item of args) {
    sum += item;
  }
  console.log(sum);
}
