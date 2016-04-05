#!/bin/bash
for file in `ls $1|grep '\(building\)'`
do
	echo $file
	fname=`echo ${file:0:${#file}}`
	echo $fname
done
