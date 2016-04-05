#!/bin/bash
if [! -d "$3"];then
	mkdir "$3"
fi
for file in `ls $1|grep '\(building\)'`
do
	#echo $file
	fname=`echo ${file:0:${#file}-4}`
	#echo $fname
	fpath=$1'/'$file
	echo $3/fname
	#sh valid_order.sh fpath $3/fname.geo.report.xml 3
done
