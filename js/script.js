const bgm1 = document.querySelector("#bgm1");       // <audio>
const btn = document.querySelector("#btn-play");   // <button>

console.log(location.hostname);

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

function gate() {
  // ▼ユーザの入力を求める
  var UserInput = prompt("パスワードを入力して下さい:", "");
  // ▼入力内容をチェック
  if (/\W+/g.test(UserInput)) {
    // ▼半角英数字以外の文字が存在したらエラー
    alert("半角英数字のみを入力して下さい。");
  }
  // ▼キャンセルをチェック
  else if (UserInput != null) {
    // ▼入力内容からファイル名を生成して移動
    location.href = UserInput + ".html";
  }
}


function push_button() {
  document.location.href = "templates/nowtime/nowtime.html";
}

function cookie_tests() {
  document.cookie = "aaa"
}

function music_play() {
  document.location.href = "templates/Musicplay/index.html"
}
function homeback() {
  location.href = "/";
}