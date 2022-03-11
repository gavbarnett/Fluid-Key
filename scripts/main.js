
function KeyboardInit()
{
	var canvas = document.getElementById("keyboard-canvas");
	var ctx = canvas.getContext("2d");
	ctx.font = "30px Arial";
	ctx.fillStyle = "#999999";
	ctx.fillText(predict["__ngrams__"]["__letters__"]["a"]["__count__"], canvas.clientWidth/10, canvas.clientHeight/2);
}

function main()
{
	KeyboardInit()
}
