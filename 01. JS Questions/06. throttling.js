/**
 * Throttling is used to call a function after every millisecond or a particular interval of time only the first click is executed immediately.
 * However the second time the func call, if the delay period has not completed, the cb function won't execute immediately. Instead it's execure the cb func once the delay has been completed.
 */

function throttle(cb, delay) {
  // lastCalledTime = 0, is because to execute the cb function immediately first time.
  let lastCalledTime = 0;
  let timerId;

  const throttledFunction = function (...args) {
    const currentTime = Date.now();
    const timeSinceLastCall = currentTime - lastCalledTime;
    const delayRemaining = delay - timeSinceLastCall;
    if (delayRemaining <= 0) {
      lastCalledTime = currentTime;
      // 'this' refered to the context, created by the throttledFunction.
      cb.apply(this, args);
    } else {
      clearTimeout(timerId);
      // In this case, can't call the cb function immediately.
      timerId = setTimeout(() => {
        lastCalledTime = Date.now();
        cb.apply(this, args);
      }, delayRemaining);
    }
  };

  throttledFunction.cancel = function () {
    clearTimeout(timerId);
  };

  return throttle;
}
