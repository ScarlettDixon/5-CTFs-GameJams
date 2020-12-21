#!/bin/bash

i=1

outname='./responses/out'
outfile="${outname}${i}"

echo $i > cookie.txt
echo -n "$(cat $outfile | grep Set-Cookie | cut -c23-48)" >> cookie.txt