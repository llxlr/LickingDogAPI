function click() {
    swal.queue([{
        title: '访问统计',
        confirmButtonText: '详情',
        text:
            '显示详情，' +
            '通过AJAX请求',
        showLoaderOnConfirm: true,
        preConfirm: function () {
            return new Promise(function (resolve) {
                // $.get('https://api.ipify.org?format=json')
                $.get('/log/')
                    .done(function (data) {
                        swal.insertQueueStep(data.ts)
                        resolve()
                    })
            })
        }
    }])
}

function dark() {
    if (document.getElementsByTagName('body')[0].className=='night') {
        document.getElementsByTagName('body')[0].classList.remove("night");
        console.log('夜间主题关闭');
    } else {
        document.getElementsByTagName('body')[0].classList.add("night");
        console.log('夜间主题开启');
    }
}
