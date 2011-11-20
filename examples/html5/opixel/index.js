// screen references
var bx = $("#bx");
var ctx = bx[0].getContext("2d");
// world instantiation
var op = new OpWorld({
	viewport : {
		w : 800,
		h : 600
	},
	root : "../../../layers",
	ctx : ctx
});
op.addSprite(new Sprite({
	layers : [ //
	op.imgarr[2], //
	op.imgarr[15], //
	op.imgarr[17], //
	op.imgarr[27],//
	op.imgarr[48] //
	],
	controller : new MouseController({
		element : bx
	})
}));

var paused = false;

function loop() {
	setTimeout(function() {
		d2 = new Date().getTime();
		delta = d2 - d1;
		op.step(delta);
		if (!paused)
			loop();
	}, 1.0 / 30.0);
	d1 = new Date().getTime();
}

loop();