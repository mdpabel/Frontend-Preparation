import './style.css';

const accordionHeaders = document.querySelectorAll('.header');
const accordionBodies = document.querySelectorAll('.body');

(() => {
  accordionHeaders.forEach((accordionHeader) => {
    accordionHeader.addEventListener('click', () => {
      accordionHeader.classList.toggle('show');

      const accordionBody = accordionHeader.nextElementSibling;

      if (!accordionHeader.classList.contains('show')) {
        accordionBody.style.height = '0px';
      } else {
        resetPreviousState(accordionBody);
        accordionBody.style.height = accordionBody.scrollHeight + 'px';
      }
    });
  });
})();

function resetPreviousState(accordionBody) {
  accordionBodies.forEach((ab) => {
    if (ab !== accordionBody) {
      ab.style.height = '0px';
      ab.previousElementSibling.classList.remove('show');
    }
  });
}
