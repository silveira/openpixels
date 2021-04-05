![example](https://raw.githubusercontent.com/silveira/openpixels/master/examples/images/we_are_hiring.png "Example of use of OpenPixels tiles and characters")

For more details http://silveiraneto.net/tag/pixelart

# Getting OpenPixels
http://silveiraneto.net/2011/08/20/getting-openpixels/

# Games using OpenPixels
* Esc 4 Home by  [Zendrael](http://www.zendrael.com/)
 * [Chrome Web Store](https://chrome.google.com/webstore/detail/esc-4-home/ooomgapfmfbcdbodcamfhhmbpefpfibo)
 * [Firefox Marketplace](https://marketplace.firefox.com/app/esc-4-home/)
 * [Online in browser version](http://www.zendrael.com/games/esc4home/)

* Rec Center Tycoon
 * [Rec Center Tycoon on Steam](https://store.steampowered.com/app/623700/Rec_Center_Tycoon/)

# Layers
On the open_chars.xcf file each layer should have a name like:
TYPE_DESCRIPTION
Examples:
hair_cuttedblack
cloths_dress
Right now no spaces are allowed.
To extract xcf layers into png files first install the package xcftools.
Exemple:
sudo apt-get install xcftools
After this execute the script extract_layers.sh to the xcf file.
./extract_layers open_chars.xcf
