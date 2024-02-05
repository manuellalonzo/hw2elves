# This python program reads information from a calibration document and filters out
# and combines the first and last number in the line and then adds each combined number
# for each line to a total number.
## usage: python3 elf_cal.py calibration_doc.txt
    
# Importing the re module
import re
import sys


def elf_calibration():

    if len(sys.argv) < 2:
        print('You failed to provide input file on command line. usage: python elf.py inputfile ')
        sys.exit(1)  # abort no input file
     
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        #print(line)
    #find if there is only one number in the calibration line
        y = sum(1 for x in line if x.isdigit())
      
    #find the first number in string
        firstnum = re.search(r'[0-9]+', line[::1])
    #Finding last number in string
        lastnum = re.search(r'[0-9]+', line[::-1])

        if y == 1:
            print('calibration number is:', firstnum.group()[::1])
            num = (firstnum.group()[::1])
            total = total + int(num)
            
        elif lastnum or firstnum:
            num =((firstnum.group()[::1]) + (lastnum.group()[::-1]))
            print('calibration number is:', num)
            total = total + int(num) 
       
        else:
            print('The given string does not have any number ')

    print('the Total of the calibration numbers is:', total)

elf_calibration()
