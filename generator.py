# Imports
import os
from PIL import Image
from random import choice

# Functions
def dirFiles(dname):
	"""Return a list of files from a passed directory path."""
	fileList = []
	for r,d,f in os.walk(dname):
		for afile in f:
			afile = str(os.path.join(r,afile)).replace("\\", "/")
			fileList.append(afile)
	return fileList

def compose(layerList):
	img = None
	for layer in layerList:
		if img == None:
			img = Image.open(layer)
			continue
		layerObj = Image.open(layer)
		img.paste(layerObj, (0,0), mask=layerObj)
	return img

# Main
for i in range(50):
	layers = []
	layers.append( choice(dirFiles("layers/body")) )
	layers.append( choice(dirFiles("layers/cloths")) )
	layers.append( choice(dirFiles("layers/eyes")) )
	layers.append( choice(dirFiles("layers/hair")) )
	layers.append( choice(dirFiles("layers/hat")) )
	layers.append( choice(dirFiles("layers/misc")) )
	compose(layers).save("export/export"+str(i)+".png", "PNG")