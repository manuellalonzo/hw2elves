# This is a bash program which reads from a calibration document and filters 
# out and combines the first and last number in a line and then adds each combined number 
# for each 3rd line into a total. "usage: ./elf.sh inputfile" 
# make sure you run chmod 755 elf.sh so that it execute authority to run.

#!/bin/bash
filename=$1
sum=0
if [  -z "$filename" ]; then
     echo "please add input file - usage: ./elf.sh inputfile"
     exit
fi

while read -r line
do 
	#The sed line filters out all non numeric characters and then awk prints the first 
	#and last numbers in a line. 	
	num=$( echo "$line" | sed 's/[^0-9]\+/ /g' | awk  '{ print $1 $NF }')
        echo "calibration number is: ${num}"
        sum=`expr $sum + $num`        
done <<< "$(sed -n '0~3p' ${filename})"

echo "Total of the calibration numbers is: ${sum}"
