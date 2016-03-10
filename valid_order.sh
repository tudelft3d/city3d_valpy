#!/bin/bash
currentpath=$(cd `dirname $0`; pwd)
outputfile=$currentpath/result/$2
#echo $outputfile
/Users/octeufer/Work/val3dity/val3dity $1 --oxml $outputfile
filename=${outputfile##*/}
#echo $filename
output=`echo "$filename"|awk -F'.' '{printf("%s.semantic.%s.%s",$1,$3,$4)}'`
#echo $output
python semantic_check.py $1 $3 $outputfile > $currentpath/result/$output
