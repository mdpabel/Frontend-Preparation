import { getData, debounced } from './utils';

const searchBox = document.getElementById('search__box');
const suggestionWrapper = document.getElementById('suggestion__wrapper');

const resetState = () => {
  suggestionWrapper.classList.remove('suggestion__visible');
  suggestionWrapper.innerHTML = '';
};

const renderDropDown = (result) => {
  const ul = document.createElement('ul');
  ul.classList.add('search_lists');

  result?.forEach((el) => {
    const li = document.createElement('li');
    li.innerHTML = el.name;
    li.classList.add('search_list');
    li.setAttribute('data-key', el.name);
    ul.appendChild(li);
  });

  suggestionWrapper.innerHTML = '';
  suggestionWrapper.appendChild(ul);
};

const handleSearch = async (keyWord) => {
  const result = await getData(keyWord);
  console.log(result, keyWord);
  if (result.length) {
    suggestionWrapper.classList.add('suggestion__visible');
    renderDropDown(result);
  } else {
    resetState();
  }
};

const onInputChange = (event) => {
  const value = event.target.value;
  if (value) {
    handleSearch(value);
  } else {
    resetState();
  }
};

const onClickList = (event) => {
  const { key } = event.target.dataset;
  if (key) {
    searchBox.value = key;
    resetState();
  }
};

(() => {
  searchBox.addEventListener('input', debounced(onInputChange, 300));
  suggestionWrapper.addEventListener('click', onClickList);
})();
