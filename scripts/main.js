
function KeyboardInit()
{
	var canvas = document.getElementById("Keyboard-Canvas");
	var ctx = canvas.getContext("2d");
	ctx.font = "30px Arial";
	ctx.fillText("H", canvas.clientWidth/10, canvas.clientHeight/2);
}

function main()
{
	KeyboardInit()
}
