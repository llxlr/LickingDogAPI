//log
function readlog() {
    $.ajax({
        url: "/v1/log/",
        type: "get",
        dataType: "json",
        success: function(data, status) {
            data = data.data;
            alert('接口总请求数'+data.pv+'总用户访问数'+data.uv+'总页面访问量'+data.ts);
            // swal.fire([{
            //     icon: 'info',
            //     title: '访问统计',
            //     text: '接口总请求数'+data.pv+'总用户访问数'+data.uv+'总页面访问量'+data.ts,
            //     showConfirmButton: false,
            //     timer: 2000
            // }])
        }
    });
}

//夜间模式
function dark() {
    let body = document.getElementsByTagName('body');
    if (body[0].className==='night') {
        body[0].classList.remove("night");
    } else {
        body[0].classList.add("night");
    }
}

// 响应耗时
function ResTime(){
    let ResTime = window.performance;
    function RAM(size) { return Math.floor(size / 1024 / 1024, 4) + 'MB'; }
    function consume(time) { return time + 'ms'; }
    let data = {
        'ram':RAM(ResTime.memory.usedJSHeapSize),
        'tcp':consume(ResTime.timing.connectEnd - ResTime.timing.connectStart),
        'res':consume(ResTime.timing.responseEnd - ResTime.timing.responseStart),
    };
    window.onload = function() {
        console.log("dom渲染耗时：" + consume(ResTime.timing.domComplete - ResTime.timing.domLoading));
    }
    return data;
}

