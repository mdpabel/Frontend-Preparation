import { countries } from './data';

export const getData = async (keyword) => {
  const data = countries.filter(
    ({ name }) =>
      name.substring(0, keyword.length).toLowerCase() == keyword.toLowerCase()
  );

  return new Promise((resolve) => setTimeout(() => resolve(data), 500));
};

export const debounced = (cb, delay = 500) => {
  let timerId;
  return function (...args) {
    clearInterval(timerId);
    timerId = setTimeout(() => cb.apply(this, args), delay);
  };
};
