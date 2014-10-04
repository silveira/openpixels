all: extract_char_layers crop_tileset things

extract_char_layers:
	./extract_layers.sh open_chars.xcf

depends_imagemagick: ; @which convert > /dev/null

crop_tileset: depends_imagemagick things_dir

things_dir:
	${mkdir things}

refrigerator:
	convert open_tileset.png -crop 31x61+0+97 things/refrigerator.png

stove:
	convert open_tileset.png -crop 31x44+32+113 things/stove.png

things: refrigerator stove
