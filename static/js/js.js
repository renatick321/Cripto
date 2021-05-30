var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementsByClassName("header")[0].style.top = "0";
  } else {
    document.getElementsByClassName("header")[0].style.top = "-60px";
  }
  prevScrollpos = currentScrollPos;
}

ResultInput = function(val) {
	container = document.getElementsByClassName("container")[0];
	result1 = container.getElementsByClassName("row")[2].getElementsByClassName("row")[1].getElementsByClassName("col-xs-12")[0];
	result2 = container.getElementsByClassName("row")[2].getElementsByClassName("row")[3].getElementsByClassName("col-xs-12")[0];
	result3 = container.getElementsByClassName("row")[7].getElementsByClassName("row")[1].getElementsByClassName("col-xs-12")[0];
	result1.innerText = "Итог: " + (val*1.2).toFixed(0).toString(10) + " ₽";
	result2.innerText = "Итог: " + (val*20).toFixed(0).toString(10) + " ₽";
	result3.innerText = "Итог: " + (val*50).toFixed(0).toString(10) + " ₽";
};