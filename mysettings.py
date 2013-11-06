## Current Temperature Log ##
#############################
## Run or kill ##
run = 1
## Temperature Settings ##
cool_on = 73
cool_off = 69
tran_on = 73
tran_off = 69
heat_on = 68
heat_off = 71
## Mode Settings ##
cool = 70
tran_1 = 69.99999999
tran_2 = 65.00000001
heat = 65
## Temperature readings ##
bedroom_1 = 60
bedroom_2 = 70
office = 73
livingroom = 73
external_temp = 75
## Time Settings ##
import time
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
## other settings ##
bedrooms_sum = bedroom_1 + bedroom_2
bedrooms = bedrooms_sum / 2
house_sum = bedroom_1 + bedroom_2 + office + livingroom
house = house_sum / 4
###################
## Kill Commands ##
if bedroom_1 >= 100:
	run = 0
if bedroom_2 >= 100:
	run = 0
if office >= 100:
	run = 0
if livingroom >= 100:
	run = 0
if bedroom_1 <= 40:
	run = 0
if bedroom_2 <= 40:
	run = 0
if office <= 40:
	run = 0
if livingroom <= 40:
	run = 0
############
## Issues ##
# when internal average temp is 
# 70 to 72 (all of 72 "72.9999"), 
# the program will break and get stuck
# in a loop at lines 57 to 59 "if house is 73:"
#
#
#
#
#
#