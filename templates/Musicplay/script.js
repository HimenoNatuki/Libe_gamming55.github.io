const bgm1 = document.querySelector("#bgm1");       // <audio>
const btn1 = document.querySelector("#btn-play1");   // <button>

btn1.addEventListener("click", () => {
    // pausedがtrue=>停止, false=>再生中
    if (!bgm1.paused) {
        btn1.innerHTML = '<span class="material-symbols-outlined">play_arrow</span>';  // 「再生ボタン」に切り替え
        bgm1.pause();
    }
    else {
        btn1.innerHTML = '<span class="material-symbols-outlined">pause</span>';  // 「一時停止ボタン」に切り替え
        bgm1.play();
    }
});

const bgm2 = document.querySelector("#bgm2");       // <audio>
const btn2 = document.querySelector("#btn-play2");   // <button>

btn2.addEventListener("click", () => {
    // pausedがtrue=>停止, false=>再生中
    if (!bgm2.paused) {
        btn2.innerHTML = '<span class="material-symbols-outlined">play_arrow</span>';  // 「再生ボタン」に切り替え
        bgm2.pause();
    }
    else {
        btn2.innerHTML = '<span class="material-symbols-outlined">pause</span>';  // 「一時停止ボタン」に切り替え
        bgm2.play();
    }
});

function backpages1() {
    history.back();
}

function backpages2(){
    location.href = "/"
}