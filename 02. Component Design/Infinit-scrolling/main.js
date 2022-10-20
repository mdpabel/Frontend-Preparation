import './style.css';

const API_BASE_URL = 'https://jsonplaceholder.typicode.com/photos';
let LIMIT = 48;
let START = 0;

const ul = document.getElementById('lists');
const threshold = document.querySelector('.threshold');

fetchPhotos();

function fetchPhotos() {
  const url = createUrl();
  window.fetch(url).then(async (res) => {
    const data = await res.json();
    START = data[data.length - 1].id;
    console.log(START);
    renderData(data);
  });
}

function renderData(data) {
  const fragment = document.createDocumentFragment();
  const start = data[0].id;
  const end = data[data.length - 1].id;
  const lastPhoto = end - start;
  data?.forEach((photo, idx) => {
    const li = document.createElement('li');
    li.classList.add('photo');
    if (idx === lastPhoto) {
      li.classList.add('last_photo');
    } else {
      li.classList.remove('last_photo');
    }
    const img = document.createElement('img');
    img.src = photo.thumbnailUrl;
    li.appendChild(img);
    fragment.appendChild(li);
  });
  ul.appendChild(fragment);
  threshold.classList.add('btnShow');
}

(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      const isIntersecting = entries[0]?.isIntersecting;
      if (isIntersecting) {
        fetchPhotos();
      }
    },
    {
      rootMargin: '1000px',
    }
  );

  observer.observe(threshold);
})();

function createUrl() {
  const url = new URL(API_BASE_URL);
  url.searchParams.set('_limit', LIMIT);
  url.searchParams.set('_start', START);

  return url;
}
