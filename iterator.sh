#!/bin/bash
if [ ! -d "../result_valsem/$3" ];then
mkdir "../result_valsem/$3"
echo "create folder $3 successful!"
fi
for file in `find $1|xargs ls -d|grep '\('$2'\)'`
do
	bname=`basename $file`
	fname=`echo ${bname:0:${#bname}-4}`
	semanticflag=`grep -c -E 'WallSurface|RoofSurface|GroundSurface' $file`
	if [ "$semanticflag" -gt "0" ];then
	/home/dxin/valsem/valsem $file --oxml "../result_valsem/$3/"$fname".sem.report.xml"
	fi
done
python report_aggregate.py $3> ../result/$3/sem_report.xml

