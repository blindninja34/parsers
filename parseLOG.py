#!/usr/bin/env python

print ('Inpute date (e.g. "-27.07.2017 "):')
date = input()
print ('Inpute start time (e.g. " 14:"):')
starttime = input()
print ('Inpute end time (e.g. " 14:"):')
endtime = input()
linesnumber = 0
bufer = 0
bufer2 = 0
bufer3 = 0
startpoint = 0
counter = 0
logfile = open('Applogs.txt')
parsefile = open('result.txt', 'w')
stringlist = []
data = []
for lines in logfile:
	data.append(lines)
logfile.close
for lines in data:
	linesnumber = linesnumber + 1
for i in range(linesnumber):
	if 'ASTM <Info> : Frames' in data[i]:
		counter = 0
	bufer = str(i)
	if counter == 1:
		stringlist.append(bufer)
	if str(date) in data[i]:
		if str(starttime) in data[i]:
			if 'SendMessageStrings' in data[i+1]:
				counter = 1

for i in range (len(stringlist)):
	bufer3 = int(stringlist[i])
	parsefile.write(data[bufer3-1])

parsefile.close
				
