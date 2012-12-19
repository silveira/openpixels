# Imports
import os
import argparse
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
	"""Returns layered image from a passed list image paths."""
	img = None
	for layer in layerList:
		# Set first image to background
		if img == None:
			img = Image.open(layer)
			continue
		# Ignore skipped layer
		elif layer == None:
			continue
		# Add all aditional images to that background
		layerObj = Image.open(layer)
		img.paste(layerObj, (0,0), mask=layerObj)
	return img

def generate(body = True, cloths = True, eyes = True, hair = True, hat = True, acc = True, shadow = False, shoes = False):
	"""Generates a character based on the passed arguments."""
	
	# Get paths to all layer images
	body_files = dirFiles("layers/body")
	cloths_files = dirFiles("layers/cloths")
	eyes_files = dirFiles("layers/eyes")
	hair_files = dirFiles("layers/hair")
	hat_files = dirFiles("layers/hat")
	acc_files = dirFiles("layers/accessories")

	# Generate layers
	layers = []
	if shadow: layers.append( "layers/shadow.png" )
	layers.append( file_in_dir(body_files, body) )
	layers.append( file_in_dir(cloths_files, cloths) )
	layers.append( "layers/eyeballs.png" )
	layers.append( file_in_dir(eyes_files, eyes) )
	layers.append( file_in_dir(hair_files, hair) )
	layers.append( file_in_dir(cloths_files, hat) )
	layers.append( file_in_dir(acc_files, acc) )
	if shoes: layers.append( "layers/shoes.png" )

	# Compose and return
	return compose(layers)

def file_in_dir(paths, search_str):
	if not search_str: return None
	elif str(search_str) == "Any":
	 	return choice(paths)
	for path in paths:
		if path.find(str(search_str)) != -1: return path
	return choice(paths)


# Main Command Line
parser = argparse.ArgumentParser(description='Generate character assets.')
parser.add_argument("number", type=int, help="number of characters to generate")
parser.add_argument("export", help="export directory", default="export/")

# Optional Arguments
parser.add_argument("-body", help="show body", default=True)
parser.add_argument("-cloth", help="show cloths", default=False)
parser.add_argument("-eye", help="show eyes", default=False)
parser.add_argument("-hair", help="show hair", default=False)
parser.add_argument("-hat", help="show hats", default=False)
parser.add_argument("-acc", help="show accessories", default=False)

# Optional Arguments
parser.add_argument("-shadow", help="show drop shadown", action="store_true", default=False)
parser.add_argument("-shoe", help="show shoes", action="store_true", default=False)

# Parse Arguments
args = parser.parse_args()

# Main
for i in range(args.number):
	char = generate(args.body, args.cloth, args.eye, args.hair, args.hat, args.acc, args.shadow, args.shoe)
	char.save(args.export+str(i)+".png", "PNG")
	print("Saving '"+"export/export"+str(i)+".png"+"'")