//디지털 시계
setInterval(myWatch, 1000)      //초 간격으로 시간설정


function myWatch(){     //날짜 간격으로 객체 생성
    var date = new Date;
    var now = date.toLocaleTimeString();
    document.getElementById('display').innerHTML = now
}