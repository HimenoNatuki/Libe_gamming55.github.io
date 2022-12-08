const bgm1 = document.querySelector("#bgm1");       // <audio>
const btn = document.querySelector("#btn-play");   // <button>

btn.addEventListener("click", () => {
  // pausedがtrue=>停止, false=>再生中
  if (!bgm1.paused) {
    btn.innerHTML = '<i class="fas fa-play">再生</i>';  // 「再生ボタン」に切り替え
    bgm1.pause();
  }
  else {
    btn.innerHTML = '<i class="fas fa-pause">停止</i>';  // 「一時停止ボタン」に切り替え
    bgm1.play();
  }
});

function push_button() {
  document.location.href = "templates/nowtime/nowtime.html";
}

function cookie_tests() {
  document.cookie = "aaa"
}
function camera_redirectd_(){
  document.location.href="templates/testcamera/index.html"
}