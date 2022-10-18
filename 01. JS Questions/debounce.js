/**
 * This is a higher order function, return transform version of cb function.
 * This cb function should wait delay milliseconds before it is invoked
 */

function debounce(cb, delay) {
  // we need to save timerId b/w func call, the timerId should be same for each call to this returned func.
  // So we need to use the clousure to do this
  let timerId;
  return function (...args) {
    // If the function call again before delay, then simply reset the delay,
    // so that func wouldn't be execite before delay ms of passed since last it was called
    clearTimeout(timerId);
    // Binding `this`.
    // setTimeout execute cb func is diff context.
    timerId = setTimeout(() => cb.apply(this, args), delay);
  };
}
