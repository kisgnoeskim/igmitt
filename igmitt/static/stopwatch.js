let timerId;
let time = loadSavedTime(); // 초기값을 저장된 시간으로 설정
const stopwatch = document.getElementById("stopwatch");
let hour, min, sec;

function printTime() {
    time++;
    updateDisplay();
    saveTime(time); // 시간 업데이트 시 로컬 스토리지에 저장
}

// 시계 시작
function startClock() {
    stopClock();
    timerId = setInterval(printTime, 1000);
}

// 시계 중지
function stopClock() {
    clearInterval(timerId);
}

// 시계 초기화
function resetClock() {
    stopClock();
    time = 0;
    updateDisplay();
    saveTime(time); // 초기화 시 로컬 스토리지에 저장
}

// 시간을 화면에 업데이트하는 함수
function updateDisplay() {
    stopwatch.innerText = getTimeFormatString();
}

// 시간(int)을 시, 분, 초 문자열로 변환
function getTimeFormatString() {
    hour = parseInt(String(time / (60 * 60)));
    min = parseInt(String((time - (hour * 60 * 60)) / 60));
    sec = time % 60;

    return String(hour).padStart(2, '0') + ":" + String(min).padStart(2, '0') + ":" + String(sec).padStart(2, '0');
}

// 저장된 시간을 불러오는 함수 추가
function loadSavedTime() {
    const savedTime = localStorage.getItem('elapsed_time');
    return savedTime ? parseInt(savedTime) : 0;
}

// 저장된 시간을 로컬 스토리지에 저장하는 함수 추가
function saveTime(time) {
    localStorage.setItem('elapsed_time', time);
}

// 페이지 로딩 시 저장된 시간을 불러오도록 호출
loadSavedTime();
updateDisplay(); // 초기 시간을 표시
