"""
Here is a Pygame Sprite [1] animation using the approach presented by Joe Wreschnig [2] and Nicolas Crovatti [3].
1. http://www.pygame.org/docs/ref/sprite.html
2. http://www.sacredchao.net/~piman/writing/sprite-tutorial.shtml
3. http://blog.shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
"""

import pygame, random
from pygame.locals import *
 
class Char(pygame.sprite.Sprite):
	x,y = (100,0)
	def __init__(self, img, frames=1, modes=1, w=32, h=32, fps=3):
		pygame.sprite.Sprite.__init__(self)
		original_width, original_height = img.get_size()
		self._w = w
		self._h = h
		self._framelist = []
		for i in xrange(int(original_width/w)):
			self._framelist.append(img.subsurface((i*w,0,w,h)))
		self.image = self._framelist[0]
		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0
		self.update(pygame.time.get_ticks(), 100, 100)
 
	def set_pos(self, x, y):
		self.x = x
		self.y = y
 
	def get_pos(self):
		return (self.x,self.y)
 
	def update(self, t, width, height):
		# postion
		self.y+=1
		if(self.y>width):
			self.x = random.randint(0,height-self._w)
			self.y = -self._h
 
		# animation
		if t - self._last_update > self._delay:
			self._frame += 1
			if self._frame >= len(self._framelist):
				self._frame = 0
			self.image = self._framelist[self._frame]
			self._last_update = t
 
SCREEN_W, SCREEN_H = (320, 320)
 
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
	background = pygame.image.load("field.png")
	img_orc = pygame.image.load("orc.png")
	orc = Char(img_orc, 4, 1, 32, 48)
	while pygame.event.poll().type != KEYDOWN:
		screen.blit(background, (0,0))
		screen.blit(orc.image,  orc.get_pos())
		orc.update(pygame.time.get_ticks(), SCREEN_W, SCREEN_H)
		pygame.display.update()
		pygame.time.delay(10)
 
if __name__ == '__main__': main()
