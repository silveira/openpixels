/**
 * Openpixels example in Processing.
 * This simple example of how to get a sprite 
 * from a sprite sheet.
 */

PImage bg;
PImage sprite_sheet;
PImage player;

void setup() { 
  // load images
  bg = loadImage("kitchen.png");
  sprite_sheet = loadImage("guy.png");
  
  /* The sprite size is 32x49.
     Look guy.png, the "stand position" is at (36,102). */
  
  player = createImage(32, 49, ARGB);
  player.copy(sprite_sheet, 36, 102, 32, 49, 0, 0, 32, 49);

  // set screen size and background
  size(bg.width, bg.height);  
  background(bg);
  
  frameRate(30);
}

void draw() { 
  background(bg);
  image(player, 100, 50);
}
