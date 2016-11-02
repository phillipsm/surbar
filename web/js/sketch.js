function setup() {
    createCanvas(windowWidth, windowHeight);
    stroke('#222');
    noLoop();
}

function draw() {
		var color_picker;
	for (i=0; i<windowHeight; i++) {
		color_picker = int(floor(random(0,10)));

		if (color_picker < 7) {
    		stroke('#00363F');
		} else if (color_picker == 7) {
			stroke('#b0ff30');
		} else {
			stroke('#83edff');
		}

		strokeWeight(int(floor(random(1,1.2))));

		var x = random(0, windowWidth);
		var y = random(0, windowHeight);
		line(x, y, x + random(windowHeight/random(-2,-5), windowHeight/random(2,5)), y);
	}
}    
