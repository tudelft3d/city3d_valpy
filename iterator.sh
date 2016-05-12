#!/bin/bash
if [ ! -d "../result/$3" ];then
mkdir "../result/$3"
echo "create folder $3 successful!"
fi
# echo '\('$2'\)'
for file in `ls $1|grep '\('$2'\)'`
do
	#echo $file
	fname=`echo ${file:0:${#file}-4}`
	#echo $fname
	fpath=$1'/'$file
	#echo $3/fname
	#echo $3/$fname".geo.report.xml"
	semanticflag=`grep -c -E 'WallSurface|RoofSurface|GroundSurface' $fpath`
	if [ "$semanticflag" -gt "0" ];then
	sh valid_order.sh $fpath $fname".geo.report.xml" 3 $3
	fi
done
python report_aggregate.py $3> ../result/$3/report.xml

