#!/bin/sh

# TODO check if xcfinfo and xcf2png exists

# TODO put a -v --verbose option
# check if we have the parameter
if [ $# -ne 1 ]
then
	echo "Usage:"
	echo "\t$0 FILE"
	exit
fi

# the first parameter is a xcf filename
filename=$1

# use xcfinfo first line to retrieve the number of the layers in the XCF file
layers_count=`xcfinfo $filename | head -1 | cut -d',' -f3 | cut -d' ' -f2`

# use xcfinfo to retrieve the name of each layer. use layers_count to ignore the first line.
# layers can NOT have spaces in the name
layers_names=`xcfinfo $filename | cut -d' ' -f5 | tail -$(($layers_count))`

# directory to put layers
destdir='layers'
mkdir $destdir 2>> /dev/null

# extract layer by layer as a png using xcf2png
for layer_name in $layers_names
do
	command="xcf2png $filename $layer_name --output $layer_name.png"
	echo -n "Extracting $layer_name... "
	$command
	if [ $? -eq 0 ]
	then
		mv $layer_name.png $destdir
		echo "OK"
	else 
		echo "FAIL"
		echo "Problem executing: $command"
	fi
done

# TODO count how many layers were succesfully extracted
# TODO use layer's alpha level

