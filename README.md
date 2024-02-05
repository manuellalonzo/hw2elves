# hw2elves
These programs run against an elf calibration document in order to get the correct calibration values and then creates a total of these values. there are two programs one bash and one python. This python program reads information from a calibration document and filters out and combines the first and last calibration number/value in the line and then adds each combined number for each line to a total number. usage: python elf_cal.py calibration_doc.txt

The second program is a bash program. It reads from a calibration document and filters out and combines the first and last number in a line and then adds each combined number for each 3rd line into a total. "usage: ./elf.sh inputfile"
