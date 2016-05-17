#!/bin/bash
currentpath=$(cd `dirname $0`; pwd)
outputfile="../result/$4/$2"
#outputfile=../result/$4/$2
#echo $outputfile
/home/dxin/val3dity/val3dity $1 -p MS --oxml $outputfile
filename=${outputfile##*/}
#echo $filename
output=`echo "$filename"|awk -F'.' '{printf("%s.semantic.%s.%s",$1,$3,$4)}'`
#echo $output
python semantic_check.py $1 $3 $outputfile > $currentpath/../result/$4/$output
