function dark() {
	if (document.getElementsByTagName('body')[0].className=='night') {
		document.getElementsByTagName('body')[0].classList.remove("night");
		console.log('夜间主题关闭');
	} else {
		document.getElementsByTagName('body')[0].classList.add("night");
		console.log('夜间主题开启');
	}
}