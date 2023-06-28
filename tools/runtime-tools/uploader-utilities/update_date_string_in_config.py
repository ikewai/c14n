#!/usr/bin/env python3
# update_date_string_in_config.py
# usage: python3 update_date_string_in_config.py inputfile outputfile [custom_date]
# This script will use yesterday's date (or a custom date if provided) to replace %y with the year, %m with the month, and %d with the day
# for all occurrences in the inputfile and then have the actual dates in the outputfile.
# The inputfile and outputfile are required arguments, while the custom_date argument is optional.
# If the custom_date argument is provided, it must be in ISO format (YYYY-MM-DD).
# Example usage: python3 update_date_string_in_config.py input.txt output.txt 2022-01-01
import sys
import datetime

dtToday = datetime.datetime.today()
dtYesterday = dtToday - datetime.timedelta(days=1)

print(f"Updating date strings in {sys.argv[1]}")

#input file
fin = open(sys.argv[1], "rt")
#output file to write the result to
fout = open(sys.argv[2], "wt")
#for each line in the input file

# Check if a custom date was provided, and read it if so.
custom_time: bool = False
custom_time_datetime: datetime.datetime = datetime.datetime.today() # default to today
if len(sys.argv) > 3:
    custom_time = True
    custom_time_str: str = str(sys.argv[3])
    custom_time_datetime: datetime.datetime = datetime.datetime.fromisoformat(custom_time_str)

# Ensure that there's a preceding zero for single-digit months/days.
def date_preceding_zero(input: int):
    if input < 10:
        return f"0{input}"
    else:
        return str(input)

for line in fin:
	#read the input file, replace each date string, and write to output file
    if custom_time:
        newline = line.replace('%y', str(custom_time_datetime.year))
        newline = newline.replace('%m', date_preceding_zero(custom_time_datetime.month))
        newline = newline.replace('%d', date_preceding_zero(custom_time_datetime.day))
    else:
        newline = line.replace('%y', str(dtYesterday.year))
        newline = newline.replace('%m', date_preceding_zero(dtYesterday.month))
        newline = newline.replace('%d', date_preceding_zero(dtYesterday.day))
    fout.write(newline)
print(f"Saved as {sys.argv[2]}")

#close input and output files
fin.close()
fout.close()
