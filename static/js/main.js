function click() {
  $.ajax({
    url: "/log/",
    type: "get",
    dataType: "json",
    success: function(data) {
      console.log(data);
      swal.fire([{
        icon: 'info',
        title: '访问统计',
        text: '接口总请求数'+data.pv+'总用户访问数'+data.uv+'总页面访问量'+data.ts,
        showConfirmButton: false,
        timer: 2000
      }])
    }
  });
}

function dark() {
    let body = document.getElementsByTagName('body');
    if (body[0].className==='night') {
        body[0].classList.remove("night");
        console.log('夜间主题关闭');
    } else {
        body[0].classList.add("night");
        console.log('夜间主题开启');
    }
}
