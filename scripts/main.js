
function NgramSort(input)
{
	ordered_keys = []
	ordered_keys = Object.keys(input).sort((a,b) => input[b]["__count__"]-input[a]["__count__"])
	ordered_keys = ordered_keys.filter(function(value){return(!(value.includes("__")))})
	console.log(ordered_keys)
	return (ordered_keys)
}

function KeyboardInit(maxdepth, rows)
{
	ordered_letters = NgramSort(predict["__ngrams__"]["__letters__"])
	AddLetters(ordered_letters, maxdepth, 1, rows)
	return (predict["__ngrams__"]["__letters__"])
}

function AddLetters(letters, maxdepth, depth, rows)
{
	var canvas = document.getElementById("keyboard-canvas");
	var ctx = canvas.getContext("2d");
	ctx.font = "20px Arial";
	ctx.fillStyle = "#999999";
	for (x=0; x<=Math.min((ordered_keys.length),rows); x++)
	{
		ctx.fillText(ordered_letters[x], canvas.clientWidth/maxdepth*depth, canvas.clientHeight/(rows+2)*(x+0.5))
	}
}

function KeyboardSubmit()
{

}

function KeyboardNextLetter(maxdepth, depth, rows, dict, key)
{
	ordered_letters = NgramSort(dict[key])
	AddLetters(ordered_letters, maxdepth, depth, rows)
	return (dict[key])
}

function main()
{
	maxdepth = 10
	rows = 6
	depth = 1
	dict = KeyboardInit(maxdepth, rows)
	//fake select letters
	depth += 1
	key = "t"
	dict = KeyboardNextLetter(maxdepth, depth, rows, dict, key)
	depth += 1
	key = "h"
	dict = KeyboardNextLetter(maxdepth, depth, rows, dict, key)
	depth += 1
	key = "e"
	dict = KeyboardNextLetter(maxdepth, depth, rows, dict, key)
	
}
