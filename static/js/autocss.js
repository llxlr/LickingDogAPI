var now = new Date(),var hour = now.getHours(),
var head = document.getElementsByTagName('head')[0],
var URL = 'https://unpkg.com/docsify/themes/',
var cssList = new Array( "vue.css","buble.css","dark.css", "pure.css", "dolphin.css"),
var link = document.createElement('link');
link.rel = "stylesheet";
if(hour>6&&hour<22){link.href = URL + cssList[1];}else{link.href = URL + cssList[2];}
window.onload = function(link){head.appendChild(link);}