all: extract_char_layers crop_tileset things

extract_char_layers:
	./extract_layers.sh open_chars.xcf

depends_imagemagick: ; @which convert > /dev/null

crop_tileset: depends_imagemagick things_dir

things_dir:
	${mkdir things}

refrigerator:
	convert open_tileset.png -crop 31x61+0+97 things/$@.png

stove:
	convert open_tileset.png -crop 31x44+32+113 things/$@.png

kitchen_table:
	convert open_tileset.png -crop 63x39+64+118 things/$@.png

sink_cabinet:
	convert open_tileset.png -crop 63x49+128+110 things/$@.png

radio:
	convert open_tileset.png -crop 32x48+192+109 things/$@.png

shelf_full:
	convert open_tileset.png -crop 64x62+224+98 things/$@.png 

shelf_empty:
	convert open_tileset.png -crop 64x62+288+98 things/$@.png 

tv:
	convert open_tileset.png -crop 31x42+352+118 things/$@.png 

vending_machine:
	convert open_tileset.png -crop 31x60+0+162 things/$@.png 

store_refrigerator:
	convert open_tileset.png -crop 64x60+32+162 things/$@.png 

things: refrigerator stove kitchen_table sink_cabinet radio shelf_full shelf_empty tv vending_machine store_refrigerator
