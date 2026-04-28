let interval;
let timerId;

const timeInput = document.getElementById('timeInput');
const progress = document.getElementById('progress');
const progressText = document.getElementById('progressText');
const startBtn = document.getElementById('startBtn');
const clearBtn = document.getElementById('clearBtn');

// Event Handler
startBtn.addEventListener('click', startProgress);
clearBtn.addEventListener('click', clearProgress);

function startProgress() {
    startBtn.disabled = true;
    duration = parseInt(timeInput.value);

    let elapsed = 0;
    timerId = setInterval(() => {
        elapsed++;

        const ratio = Math.floor((elapsed / duration) * 100);
        progress.style.width = `${ratio}%`;
        progressText.textContent = `${ratio}%`;

        if (ratio >= 100) {
            // Stop the timer
            clearInterval(timerId);
            startBtn.disabled = false;
        }
    }, 1000);
}

function clearProgress() {
    if (timerId) clearInterval(timerId);

    progress.style.width = '0%';
    timeInput.value = "";
    progressText.textContent = '0%';
}