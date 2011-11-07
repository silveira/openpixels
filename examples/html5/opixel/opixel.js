/**
 * Open Pixel's World
 * 
 * @param config.viewport
 *            screen size
 * @param config.dimension
 *            real world size
 * @param config.camera
 *            coords for positioning and translating viewport to correct wolrd
 *            location
 * @param config.root
 *            root of resources location
 * @param config.ctx
 *            drawing context 2d
 * 
 */
function OpWorld(config) {
	// índice de imagens
	var imgarr = [];
	// 0-5 corpos
	/* 00 */imgarr.push(config.root + "/body_black.png");
	/* 01 */imgarr.push(config.root + "/body_caucassian.png");
	/* 02 */imgarr.push(config.root + "/body_green.png");
	/* 03 */imgarr.push(config.root + "/body_olive.png");
	/* 04 */imgarr.push(config.root + "/body_skeleton.png");
	/* 05 */imgarr.push(config.root + "/body_stormtrooper.png");
	/* 06 */imgarr.push(config.root + "/cloths_armor.png");
	/* 07 */imgarr.push(config.root + "/cloths_blackdress.png");
	/* 08 */imgarr.push(config.root + "/cloths_blacksuit.png");
	/* 09 */imgarr.push(config.root + "/cloths_blousewithtie.png");
	/* 10 */imgarr.push(config.root + "/cloths_blueshirtstripes.png");
	/* 11 */imgarr.push(config.root + "/cloths_blueshorts.png");
	/* 12 */imgarr.push(config.root + "/cloths_femenineunderpants.png");
	/* 13 */imgarr.push(config.root + "/cloths_greendress.png");
	/* 14 */imgarr.push(config.root + "/cloths_hazmat.png");
	/* 15 */imgarr.push(config.root + "/cloths_jeans.png");
	/* 16 */imgarr.push(config.root + "/cloths_king.png");
	/* 17 */imgarr.push(config.root + "/cloths_labcoat.png");
	/* 18 */imgarr.push(config.root + "/cloths_masculineunderpants.png");
	/* 19 */imgarr.push(config.root + "/cloths_pantsleather.png");
	/* 20 */imgarr.push(config.root + "/cloths_redtshirt.png");
	/* 21 */imgarr.push(config.root + "/cloths_santa.png");
	/* 22 */imgarr.push(config.root + "/cloths_tshirt.png");
	/* 23 */imgarr.push(config.root + "/cloths_yellowCBFtshirt.png");
	/* 24 */imgarr.push(config.root + "/ETC_authors.png");
	/* 25 */imgarr.push(config.root + "/ETC_marks.png");
	/* 26 */imgarr.push(config.root + "/ETC_whitebackground.png");
	/* 27 */imgarr.push(config.root + "/eyes_black.png");
	/* 28 */imgarr.push(config.root + "/eyes_blue.png");
	/* 29 */imgarr.push(config.root + "/eyes_brown.png");
	/* 30 */imgarr.push(config.root + "/eyes_default.png");
	/* 31 */imgarr.push(config.root + "/eyes_green.png");
	/* 32 */imgarr.push(config.root + "/eyes_loves.png");
	/* 33 */imgarr.push(config.root + "/eyes_red.png");
	/* 34 */imgarr.push(config.root + "/eyes_surprise.png");
	/* 35 */imgarr.push(config.root + "/hair_afro.png");
	/* 36 */imgarr.push(config.root + "/hair_beard.png");
	/* 37 */imgarr.push(config.root + "/hair_bun.png");
	/* 38 */imgarr.push(config.root + "/hair_cuttedblack.png");
	/* 39 */imgarr.push(config.root + "/hair_fringebrown.png");
	/* 40 */imgarr.push(config.root + "/hair_longbrown.png");
	/* 41 */imgarr.push(config.root + "/hair_longwhitebeard.png");
	/* 42 */imgarr.push(config.root + "/hair_midblack.png");
	/* 43 */imgarr.push(config.root + "/hair_mustache.png");
	/* 44 */imgarr.push(config.root + "/hair_semibald.png");
	/* 45 */imgarr.push(config.root + "/hair_squared.png");
	/* 46 */imgarr.push(config.root + "/hair_whitebeard.png");
	/* 47 */imgarr.push(config.root + "/hair_white.png");
	/* 48 */imgarr.push(config.root + "/hat_mafia.png");
	/* 49 */imgarr.push(config.root + "/hat_santa.png");
	/* 50 */imgarr.push(config.root + "/hat_turban.png");
	/* 51 */imgarr.push(config.root + "/hat_witch.png");
	/* 52 */imgarr.push(config.root + "/head_crown.png");
	/* 53 */imgarr.push(config.root + "/head_hazmat.png");
	/* 54 */imgarr.push(config.root + "/head_helmet.png");
	/* 55 */imgarr.push(config.root + "/head_skeleton.png");
	/* 56 */imgarr.push(config.root + "/head_stormstrooper.png");
	/* 57 */imgarr.push(config.root + "/misc_backpack.png");
	/* 58 */imgarr.push(config.root + "/misc_blackgloves.png");
	/* 59 */imgarr.push(config.root + "/misc_cape.png");
	/* 60 */imgarr.push(config.root + "/misc_epaulettes.png");
	/* 61 */imgarr.push(config.root + "/misc_femaledatails.png");
	/* 62 */imgarr.push(config.root + "/misc_mask_medic.png");
	/* 63 */imgarr.push(config.root + "/misc_mask.png");
	/* 64 */imgarr.push(config.root + "/misc_redboxgloves.png");
	/* 65 */imgarr.push(config.root + "/misc_roundglasses.png");
	/* 66 */imgarr.push(config.root + "/misc_shadown.png");
	/* 67 */imgarr.push(config.root + "/misc_shoes.png");
	/* 68 */imgarr.push(config.root + "/misc_slapeye.png");
	/* 69 */imgarr.push(config.root + "/misc_sunglasses.png");
	/* 70 */imgarr.push(config.root + "/misc_tank.png");
	/* 71 */imgarr.push(config.root + "/misc_vendetamask.png");
	for ( var i in imgarr) {
		var img = new Image();
		img.src = imgarr[i];
		imgarr[i] = img;
	}
	// publish resource array
	this.imgarr = imgarr;
	// sprite list
	var sprites = [];

	this.step = function(delta) {
		for ( var x in sprites)
			sprites[x].step(delta);
		this.paint();
	};

	this.paint = function() {
		config.ctx.clearRect(0, 0, config.viewport.w, config.viewport.h);
		// paint bg0, bg1...
		for ( var x in sprites)
			sprites[x].paint(config.ctx);
		// paint fg0, fg1...
	};

	this.addSprite = function(s) {
		sprites.push(s);
	};
}

function Controller(config) {
	// coords
	this.canUp = false;
	this.canRight = false;
	this.canDown = false;
	this.canLeft = false;
	// flag to publish certain movement
	this.moved = false;

	this.step = function(delta, sprite, world) {

	};

	this.reset = function() {
		this.moved = false;
		this.canUp = false;
		this.canRight = false;
		this.canDown = false;
		this.canLeft = false;
	};

}

/**
 * this class depends on jQuery
 */
function MouseController(config) {
	Controller.call(this, config);
	var x = 0;
	var y = 0;
	config.element.click(function(e) {
		var a = config.element.position().left;
		var b = config.element.position().top;
		x = e.clientX - a;
		y = e.clientY - b;
	});

	this.step = function(delta, sprite, world) {
		this.reset();
		var a = x - sprite.x;
		var b = y - sprite.y;
		if (a > 1) {
			sprite.x += sprite.v * delta;
			if(!this.moved){
				this.moved = true;
				this.canRight = true;
			}
		} else if (a < -1) {
			sprite.x -= sprite.v * delta;
			if(!this.moved){
				this.moved = true;
				this.canLeft = true;
			}
		}
		if (b > 1) {
			sprite.y += sprite.v * delta;
			if(!this.moved){
				this.moved = true;
				this.canDown = true;
			}
		} else if (b < -1) {
			sprite.y -= sprite.v * delta;
			if(!this.moved){
				this.moved = true;
				this.canUp = true;
			}
		}
	};
}

/**
 * 
 * @returns
 */
function Sprite(config) {

	var idx = 0;
	var seq = [ "c", "d", "c", "e" ];
	var face = "down";
	var time = 100;
	var cur = 0;

	// public coords
	this.x = config.x || 0;
	this.y = config.y || 0;
	this.w = 35;
	this.h = 50;
	// velocity
	this.v = 0.1;
	// controller
	this.controller = config.controller || new Controller();

	var anim = {
		up : {
			d : [ 0, 0 ],
			c : [ 35, 0 ],
			e : [ 70, 0 ]
		},
		right : {
			d : [ 0, 50 ],
			c : [ 35, 50 ],
			e : [ 70, 50 ]
		},
		down : {
			d : [ 0, 100 ],
			c : [ 35, 100 ],
			e : [ 70, 100 ]
		},
		left : {
			d : [ 0, 150 ],
			c : [ 35, 150 ],
			e : [ 70, 150 ]
		},
	};

	this.step = function(delta, world) {
		if (this.controller) {
			this.controller.step(delta, this, world);
			cur += delta;
			if (this.controller.canUp) {
				face = "up";
			}
			if (this.controller.canRight) {
				face = "right";
			}
			if (this.controller.canDown) {
				face = "down";
			}
			if (this.controller.canLeft) {
				face = "left";
			}
			if (this.controller.moved) {
				if (cur > time) {
					idx = (idx + 1) % 4;
					cur = 0;
				}
			}
		}
	};

	this.paint = function(ctx) {
		var a = anim[face][seq[idx]][0];
		var b = anim[face][seq[idx]][1];
		var w = this.w;
		var h = this.h;
		for ( var i in config.layers)
			ctx.drawImage(config.layers[i], a, b, w, h, this.x, this.y, w, h);
	};
}