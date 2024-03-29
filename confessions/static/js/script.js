function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function setRandomGradient() {
  const body = document.querySelector('body');
  const color1 = getRandomColor();
  const color2 = getRandomColor();
  body.style.background = `linear-gradient(to right, ${color1}, ${color2})`;
  
  // Reset the animation after it finishes
  setTimeout(() => {
    body.style.animation = '';
  }, 4000);
}

window.addEventListener('load', () => {
  setRandomGradient();
  setInterval(setRandomGradient, 50000);
});