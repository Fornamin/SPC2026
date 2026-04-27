const num = document.getElementById('num');

const plusBtn = document.getElementById('plusBtn');
const minusBtn = document.getElementById('minusBtn');

/* Event Handler */
plusBtn.addEventListener('click', () => { 
    num.textContent = parseInt(num.textContent) + 1 });
minusBtn.addEventListener('click', () => { 
    num.textContent = parseInt(num.textContent) - 1 });
// minusBtn.addEventListener('click', function minus() { document.getElementById('num').textContent - 1 });

// textContent는 동적이라 그 상위를 const로 정의해서 쓰자