## Home Thermostat
## Version 1.0.1
#
## Setup ##
import os
import time
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT)
#GPIO.setup(14, GPIO.OUT)
#GPIO.setup(15, GPIO.OUT)
#GPIO.output(11, GPIO.HIGH)
#GPIO.output(12, GPIO.HIGH)
#GPIO.output(14, GPIO.HIGH)
#GPIO.output(15, GPIO.HIGH)
#
## Test Vairables ##
# these values are here because i dont have temperature sensors #
'''bedroom_1 = 72
bedroom_2 = 72
office = 75
livingroom = 75
external_temp = 85'''
#
## Average Zone Temperatures ##
'''bedrooms_sum = bedroom_1 + bedroom_2
bedrooms = bedrooms_sum / 2
house_sum = bedroom_1 + bedroom_2 + office + livingroom
house = house_sum / 4'''
## Thermostat Program ##
while True:
	import mysettings
	from mysettings import *
	from datetime import datetime
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute
	second = now.second
	now_date = str(month) + '/' + str(day) + '/' + str(year)
	now_time = str(hour) + ':' + str(minute) + ':' + str(second)
	print now_time
	print now_date
	print 'program running'
	while external_temp >= 70:
		import mysettings
		from mysettings import *
		bedrooms_sum = bedroom_1 + bedroom_2
		bedrooms = bedrooms_sum / 2
		house_sum = bedroom_1 + bedroom_2 + office + livingroom
		house = house_sum / 4
		print 'cool'
		if house >= 73:
			print house
			print 'ac on'
			#GPIO.output(11, GPIO.LOW)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = ' + str(house) + '\n')
			text_file.write("AC on" + ' - ' + str(now_time) + " - " + str(now_date)+ '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		#if house <= 70:
		else:
			print house
			print 'ac off'
			#GPIO.output(11, GPIO.HIGH)
			text_file = open("thermostat log.txt", "a")
			text_file.write("Temperature" ' = '+ str(house) + '\n')
			text_file.write("AC off" + ' - ' + str(now_time) + " - " + str(now_date) + '\n')
			text_file.write('\n')
			text_file.close()
			time.sleep(6)
			reload(mysettings)
		## Check Time ##
		import time
		time.sleep(0.25)
	while external_temp <= 65:
		from mysettings import *
		bedrooms_sum = bedroom_1 + bedroom_2
		bedrooms = bedrooms_sum / 2
		house_sum = bedroom_1 + bedroom_2 + office + livingroom
		house = house_sum / 4
		print 'heat'
		if house <= 68:
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
		#if house >= 71:
		else:
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
		## Check Time ##
		import time
		time.sleep(0.25)
		reload(mysettings)
## Check Time ##
import time
time.sleep(0.25)

