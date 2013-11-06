## Home Thermostat
## Version 1.0.1
#
## Setup ##
import os
'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
## GPIO 11 = AC
GPIO.setup(11, GPIO.OUT)
#
## GPIO 12 = Heat
GPIO.setup(12, GPIO.OUT)
#
## GPIO 14 = Fan
GPIO.setup(14, GPIO.OUT)
#
## GPIO 15 = "All Systems Go" LED
GPIO.setup(15, GPIO.OUT)
#
GPIO.output(11, GPIO.HIGH)
GPIO.output(12, GPIO.HIGH)
GPIO.output(14, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)'''
#
## Thermostat Program ##
import mysettings
from mysettings import *
while run is 1:
	#GPIO.output(15, GPIO.HIGH)
	import mysettings
	from mysettings import *
	print 'starting program'
	## Cool ##
	while external_temp >= cool:
		print
		print now_time
		print now_date
		print 'program running'
		from mysettings import *
		print 'cool'
		print
		if house >= cool_on:
			print
			print house
			print 'cool on'
			print
			#GPIO.output(12, GPIO.LOW)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = ' + str(house) + '\n')
			text_file.write("cool on" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		if house <= cool_off:
			print
			print house
			print 'cool off'
			print
			#GPIO.output(12, GPIO.HIGH)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = '+ str(house) + '\n')
			text_file.write("cool off" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		else:
			reload(mysettings)
			print
			print 'waiting'
			print now_time
			print now_date
			print
		## Check Time ##
		import time
		time.sleep(0.25)
		'''
	## Transition ##
	while external_temp >= tran_1 and external_temp <= tran_2:
		print
		print now_time
		print now_date
		print 'program running'
		print
		import mysettings
		from mysettings import *
		print 'Transition'
		if house >= tran_on:
			print
			print house
			print 'fan on'
			print
			#GPIO.output(14, GPIO.LOW)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = ' + str(house) + '\n')
			text_file.write("fan on" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(120)
			print 'fan off'
			print
			#GPIO.output(14, GPIO.HIGH)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = ' + str(house) + '\n')
			text_file.write("fan off" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
			text_file.write('\n')
			text_file.close()
			reload(mysettings)
			if house >= tran_on:
				print
				print 'ac on'
				print
				#GPIO.output(11, GPIO.LOW)
				text_file = open("thermostat log.txt", "a")
				text_file.write("Temperature" ' = ' + str(house) + '\n')
				text_file.write("AC on" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
				text_file.write('\n')
				text_file.close()
			time.sleep(6)
			reload(mysettings)
		if house <= tran_off:
			print
			print house
			print 'ac off'
			print
			#GPIO.output(11, GPIO.HIGH)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = '+ str(house) + '\n')
			text_file.write("AC off" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		else:
			reload(mysettings)
			print
			print 'waiting'
			print now_time
			print now_date
			print
		## Check Time ##
		import time
		time.sleep(0.25)	'''
	## Heat ##
	while external_temp <= heat:
		print now_time
		print now_date
		print 'program running'
		from mysettings import *
		print 'heat'
		if house <= heat_on:
			print house
			print 'heat on'
			#GPIO.output(12, GPIO.LOW)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = ' + str(house) + '\n')
			text_file.write("Heat on" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		if house >= heat_off:
			print house
			print 'heat off'
			#GPIO.output(12, GPIO.HIGH)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = '+ str(house) + '\n')
			text_file.write("Heat off" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		else:
			reload(mysettings)
			print
			print 'waiting'
			print now_time
			print now_date
			print
		## Check Time ##
		import time
		time.sleep(0.25)
		reload(mysettings)
	## Check Time ##
	import time
	time.sleep(0.25)
	reload(mysettings)
if run is 0:
	#GPIO.output(11, GPIO.HIGH)
	#GPIO.output(12, GPIO.HIGH)
	#GPIO.output(14, GPIO.HIGH)
	#GPIO.output(15, GPIO.HIGH)
	text_file = open("thermostat log.txt", "a")
	text_file.write("Temperature" ' = '+ str(house) + '\n')
	text_file.write("Killing Program" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
	text_file.write('\n')
	text_file.close()
	print 'killing program'