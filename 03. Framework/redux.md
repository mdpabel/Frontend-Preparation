[Code repo](https://stackblitz.com/edit/vitejs-vite-pswskh?file=main.js)

```js
const store = reducer(state, action);
// notify the subscriber
```

```js
// reducer.js
export const reducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      state = state + action.payload.val;
      break;
    case 'DECREMENT':
      state = state - action.payload.val;
      break;
  }
  return state;
};

// store.js
import { createStore } from 'redux';
import { reducer } from './reducer';

export const store = createStore(reducer);

// main.js
import { store } from './store';

console.log(store); // dispatch(action), getState(), subscribe(listener)

store.subscribe(() => {
  console.log('Store updated', store.getState());
});

store.dispatch({
  type: 'INCREMENT',
  payload: {
    val: 1,
  },
}); // Store updated 1

store.dispatch({
  type: 'DECREMENT',
  payload: {
    val: 1,
  },
}); // Store updated 0
```
