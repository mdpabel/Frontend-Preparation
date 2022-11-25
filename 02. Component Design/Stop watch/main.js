import './style.css';

let lastTimerStartTime = 0;
let millisecondsElapsedBeforeStop = 0;
let timerId;

const watch = document.getElementById('watch');
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');

startBtn.addEventListener('click', startTimer);
stopBtn.addEventListener('click', stopTimer);
resetBtn.addEventListener('click', resetTimer);

function startTimer() {
  buttonState(true, false, true);

  lastTimerStartTime = Date.now();

  timerId = requestAnimationFrame(updateTimer);
}

function stopTimer() {
  buttonState(false, true, false);
  millisecondsElapsedBeforeStop += Date.now() - lastTimerStartTime;
  cancelAnimationFrame(timerId);
}

function resetTimer() {
  buttonState(false, true, true);
  timerId = undefined;
  lastTimerStartTime = 0;
  millisecondsElapsedBeforeStop = 0;
  watch.innerText = '00:00:000';
}

function buttonState(start, stop, reset) {
  startBtn.disabled = start;
  stopBtn.disabled = stop;
  resetBtn.disabled = reset;
}

function updateTimer() {
  const milliSecondsElapsed =
    Date.now() - lastTimerStartTime + millisecondsElapsedBeforeStop;
  const secondsElapsed = milliSecondsElapsed / 1000;
  const minutesElapsed = secondsElapsed / 60;

  const milliText = formetNumber(milliSecondsElapsed % 1000, 3);
  const secondText = formetNumber(Math.floor(secondsElapsed) % 60, 2);
  const minuteText = formetNumber(Math.floor(minutesElapsed), 2);

  watch.innerText = `${minuteText}:${secondText}:${milliText}`;
  timerId = requestAnimationFrame(updateTimer);
}

function formetNumber(number, len) {
  const stringNumber = String(number);
  return stringNumber.padStart(len, '0');
}
