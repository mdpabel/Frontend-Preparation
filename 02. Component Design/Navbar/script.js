const navBtn = document.querySelector('.nav__toggle');
const links = document.querySelector('.nav__links');

navBtn.addEventListener('click', () => {
  links.classList.toggle('show__links');
});
