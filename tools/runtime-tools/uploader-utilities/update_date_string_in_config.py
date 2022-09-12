# update_date_string_in_config.py
# usage: python3 update_date_string_in_config.py inputfile outputfile
# This script will use yesterdays date to replace %y with the year %m with the month and %d with the day
# for all occurence in the inputfile and then have the actual dates in the outputfile
from operator import ne
import sys
import datetime

dtToday = datetime.datetime.today()
dtYesterday = dtToday - datetime.timedelta(days=1)

print(sys.argv[1])
print(sys.argv[2])
#input file
fin = open(sys.argv[1], "rt")
#output file to write the result to
fout = open(sys.argv[2], "wt")
#for each line in the input file

def date_preceding_zero(input: int):
    if input < 10:
        return f"0{input}"
    else:
        return str(input)

for line in fin:
	#read replace the string and write to output file
    newline = line.replace('%y', str(dtYesterday.year))
    newline = newline.replace('%m', date_preceding_zero(dtYesterday.month))
    newline = newline.replace('%d', date_preceding_zero(dtYesterday.day))
    fout.write(newline)
#close input and output files
fin.close()
fout.close()
