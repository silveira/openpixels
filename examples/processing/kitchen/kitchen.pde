
/**
 * Openpixels example in processing
 */

int rectWidth;

PImage bg;
PImage player;
PImage piece;

int player_x = 0;
int player_y = 0;

void setup() { 
  /* load images */
  bg = loadImage("kitchen.png");
  player = loadImage("guy.png");
  
  piece =  createImage(32, 49, ARGB);
  piece.copy(player, 36, 102, 32, 49, 0, 0, 32, 49);

  // screen size and background
  size(bg.width, bg.height);  
  background(bg);
  
  image(piece, player_x, player_y);
//  image(player,5,5);
  //image(piece, 0, 0);
  //rectWidth = width/4;

  frameRate(30);
}

void draw() { 
  background(bg);
  image(piece, player_x, player_y);
  
  player_x++;
  player_y++;
}

void keyPressed() {
  /*
  int keyIndex = -1;
  if (key >= 'A' && key <= 'Z') {
    keyIndex = key - 'A';
  } else if (key >= 'a' && key <= 'z') {
    keyIndex = key - 'a';
  }
  */
  /*
  if (keyIndex == -1) {
    // If it's not a letter key, clear the screen
    background(0);
  } else { 
    // It's a letter key, fill a rectangle
    fill(millis() % 255);
    float x = map(keyIndex, 0, 25, 0, width - rectWidth);
    rect(x, 0, rectWidth, height);
  }*/
}
