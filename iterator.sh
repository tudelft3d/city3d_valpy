#!/bin/bash
if [ ! -d "../result/$3" ];then
mkdir "../result/$3"
echo "create folder $3 successful!"
fi
# echo '\('$2'\)'
for file in `find $1|xargs ls -d|grep '\('$2'\)'`
do
	#echo $file
	bname=`basename $file`
	fname=`echo ${bname:0:${#bname}-4}`
	#echo $3/$fname".geo.report.xml"
	semanticflag=`grep -c -E 'WallSurface|RoofSurface|GroundSurface' $file`
	if [ "$semanticflag" -gt "0" ];then
	sh valid_order.sh $file $fname".geo.report.xml" 3 $3
	#echo "fname: "$fname
	#echo "bname: "$bname
	#echo "file: "$file
	fi
done
python report_aggregate.py $3> ../result/$3/report.xml

