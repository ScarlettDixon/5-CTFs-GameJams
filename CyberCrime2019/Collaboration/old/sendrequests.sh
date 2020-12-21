#!/bin/bash
for i in {0..99}
do
	request='./requests/request-'
	txt='.txt'
	filename="${request}${i}${txt}"
	
	outname='./responses/out'
	outfile="${outname}${i}"
	cat $filename | nc 103.cybertrial.co.uk 80 -q 1 > $outfile
	
	echo $i > cookie.txt
	echo -n "$(cat $outfile | grep Set-Cookie | cut -c23-48)" >> cookie.txt

	python buildrequest.py
	
	outname='./responses/out'
	dot='.complete'
	outfile="${outname}${i}${dot}"
	cat newrequest.txt | nc 103.cybertrial.co.uk 80 -q 3 > $outfile
done 
	
	