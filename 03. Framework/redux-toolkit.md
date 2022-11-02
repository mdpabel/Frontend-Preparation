[Code repo](https://stackblitz.com/edit/vitejs-vite-qetgvz?file=main.js)

```js
// configureStore(reducer) -> dispatch(action)

// counterSlice.js

import { createSlice } from '@reduxjs/toolkit';

const slice = createSlice({
  name: 'Counter',
  initialState: 0,
  reducers: {
    increment: (state) => state + 1,
    decrement: (state) => state - 1,
  },
});

export const reducer = slice.reducer;
export const { increment, decrement } = slice.actions;

// main.js
import { configureStore } from '@reduxjs/toolkit';
import { decrement, increment, reducer } from './counterSlice';

const store = configureStore({
  reducer: reducer,
});

store.subscribe(() => {
  console.log('Store updated', store.getState());
});

store.dispatch(increment());
store.dispatch(decrement());
```
