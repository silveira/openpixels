/**
 * Openpixels example in Processing.
 * This simple example of how to get sprites 
 * from a sprite sheet and animate them.
 */

PImage bg;
PImage sprite_sheet;
PImage player;

int frame = 0;
int frames = 4;
PImage[] down = new PImage[frames];

void setup() { 
  // load images
  bg = loadImage("kitchen.png");
  sprite_sheet = loadImage("guy.png");
  
  // load frames
  for (int i=0; i<frames; i++)
    down[i] = createImage(32, 49, ARGB);

  down[0].copy(sprite_sheet,  1, 102, 32, 49, 0, 0, 32, 49);
  down[1].copy(sprite_sheet, 36, 102, 32, 49, 0, 0, 32, 49);
  down[2].copy(sprite_sheet, 73, 102, 32, 49, 0, 0, 32, 49);
  down[3].copy(sprite_sheet, 36, 102, 32, 49, 0, 0, 32, 49);
  
  // set screen size and background
  size(bg.width, bg.height);  
  background(bg);
  
  frameRate(5);
}

void draw() { 
  background(bg);
  image(down[frame], 100, 50);
  frame = (frame+1)%frames;
}
