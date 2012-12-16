"""
Here is a Pygame Sprite [1] animation using the approach presented by Joe Wreschnig [2] and Nicolas Crovatti [3].
1. http://www.pygame.org/docs/ref/sprite.html
2. http://www.sacredchao.net/~piman/writing/sprite-tutorial.shtml
3. http://blog.shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
"""

# PEP 8: Imports should be on seperate lines.
import random
import pygame
from pygame.locals import *
 
class Char(pygame.sprite.Sprite):
	x,y = (100,0)
	def __init__(self, img, frames=1, w=32, h=32, fps=3):
		"""
		Creates an animated character sprite objects.

		Keyword arguments:
		img     -- Path to image
		frames  -- Number of frames in the sprite sheet
		w       -- Image pixel width
		h       -- Image pixel height
		fps     -- Frames per second

		"""

		# Call parent constructor
		pygame.sprite.Sprite.__init__(self)

		# Split image frames from sprite sheets
		original_width, original_height = img.get_size()
		self._w = w
		self._h = h
		self._framelist = []
		for i in range(int(original_width/w)):
			self._framelist.append(img.subsurface((i*w,0,w,h)))
		self.image = self._framelist[0]
		
		# Set timing vars
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0
		self.update(pygame.time.get_ticks(), 100, 100)

	# Mutator
	def set_pos(self, x, y):
		self.x = x
		self.y = y
 
 	# Accessor
	def get_pos(self):
		return (self.x,self.y)
 
	def update(self, t, width, height):
		"""
		Updates the displayed image.

		Keyword arguments:
		t      -- Pass pygame.time.get_ticks() so we can figure out what image to display next.
		width  -- Current window width
		height -- Current window height

		"""

		# Position
		self.y+=1
		if(self.y>width):
			self.x = random.randint(0,height-self._w)
			self.y = -self._h
 
		# Animation
		if t - self._last_update > self._delay:
			self._frame += 1
			if self._frame >= len(self._framelist):
				self._frame = 0
			self.image = self._framelist[self._frame]
			self._last_update = t

 
def main():
	# Load PyGame window
	pygame.init()
	SCREEN_W, SCREEN_H = (320, 320)
	screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
	pygame.display.set_caption("Orc Test")

	# Load art assets
	background = pygame.image.load("field.png")
	img_orc = pygame.image.load("orc.png")
	orc = Char(img_orc, 4, 32, 48)

	# Game loop
	notDone = True
	while notDone:
		# Check for exit event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	notDone = False
		# Else just make the orc walk
		screen.blit(background, (0,0))
		screen.blit(orc.image,  orc.get_pos())
		orc.update(pygame.time.get_ticks(), SCREEN_W, SCREEN_H)
		pygame.display.update()
		pygame.time.delay(10)
 
if __name__ == '__main__': main()