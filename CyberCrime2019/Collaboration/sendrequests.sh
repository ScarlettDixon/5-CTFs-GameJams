#!/bin/bash
for i in {0..99}
do
	request='./requests/request-'
	txt='.txt'
	filename="${request}${i}${txt}"
	
	outname='./responses/out'

	outfile="${outname}${i}"
	cat $filename | nc 103.cybertrial.co.uk 80 -q 1 > $outfile

	if [ $(cat ${outfile} | grep -c "302 Found") -eq 1 ]
	then
		echo "302 response - sleep time."
		cp $outfile ./302/$i.302.txt
		if [ $(cat ./302/$i.302.txt | grep -c flag) -eq 1 ]
		then
			echo " --------------- 302 response redirecting to /flag: " $i
			python getflag.py -f $filename | nc 103.cybertrial.co.uk 80 -q 1 > flag.$i.out
			python getcontent.py -f flag.$i.out > flag.$i.gzip
			gzip -d < flag.$i.gzip | grep "FLAG CODE" > flag.$i.txt
			rm flag.$i.out
			rm flag.$i.gzip
			exit
		fi
		sleep 120
		cat $filename | nc 103.cybertrial.co.uk 80 -q 1 > $outfile
	fi

	python getcontent.py -f $outfile >out.tmp.gzip

	if [ $(file out.tmp.gzip | grep -c "HTML") -eq 1 ]
	then
		echo "Still sleepy; waiting 15."
		sleep 15
		cat $filename | nc 103.cybertrial.co.uk 80 -q 1 > $outfile		
		python getcontent.py -f $outfile >out.tmp.gzip
	fi

	gzip -d < out.tmp.gzip > ${outfile}.html
	rm out.tmp.gzip

	if [ $(cat ${outfile}.html | grep -c incorrect) -eq 1 ]
	then
		echo "No match for " $i
	else
		echo " --------------- MATCH: " $i
	fi

done 
	
	