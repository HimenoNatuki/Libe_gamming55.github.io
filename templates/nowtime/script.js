window.onload = function () {
    setInterval(function () {
        var dd = new Date();
        document.getElementById("nowtime_").innerHTML = dd.toLocaleString();
    }, 1000);
}

function return_page(){
    history.back();
}