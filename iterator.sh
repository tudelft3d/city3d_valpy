#!/bin/bash
if [! -d "../result/$3"];then
	mkdir "../result/$3"
fi
for file in `ls $1|grep '\(building\)'`
do
	#echo $file
	fname=`echo ${file:0:${#file}-4}`
	#echo $fname
	fpath=$1'/'$file
	#echo $3/fname
	#echo $3/$fname".geo.report.xml"
	sh valid_order.sh $fpath $fname".geo.report.xml" 3
done
python report_aggregate.py > ../result/$3/report.xml

