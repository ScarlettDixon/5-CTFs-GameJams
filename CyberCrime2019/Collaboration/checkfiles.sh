#!/bin/bash
for i in {0..99}
do
	outname='./responses/out'
	outfile="${outname}${i}.html"
	if [ $(cat $outfile | grep -c "Level 2") -eq 1 ]
	then
		echo "Found at $i"
	fi
done