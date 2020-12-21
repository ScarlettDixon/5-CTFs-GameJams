#!/bin/bash

array=(8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy)

for item in ${array[*]}
do
	location = find . 2>&1 | grep -v "Permission denied" | grep $item
	printf $location
done