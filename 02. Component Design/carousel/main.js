const carouselImages = document.querySelector('.carousel-images');
const prevBtn = document.querySelector('.carousel-button-prev');
const nextBtn = document.querySelector('.carousel-button-next');

let idx = 0;
const numberOfImages = 3;
let intervalId;

intervalId = setInterval(scrollImage, 5000);

function scrollImage(type = 'next') {
  inCrementDecrement(type);
  carouselImages.scrollTo({
    left: idx * 800,
    behavior: 'smooth',
  });
}

prevBtn.addEventListener('click', () => {
  resetInterval();
  scrollImage('prev');
});

nextBtn.addEventListener('click', () => {
  resetInterval();
  scrollImage('next');
});

function resetInterval() {
  clearInterval(intervalId);
}

function inCrementDecrement(type) {
  if (type == 'next') {
    idx++;
    if (idx >= numberOfImages) {
      idx = 0;
    }
  } else {
    idx--;
    if (idx < 0) {
      idx = numberOfImages - 1;
    }
  }
}
