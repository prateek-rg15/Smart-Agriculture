#!/usr/bin/env python
import os
import glob
import time
import sys
import test2

class TemperatureSensing():

    def get_name(mrg):
        print   'Temperature sensor'

    

    
    def get_temperature(mrg):
            # load the kernel modules needed to handle the sensor
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')

            # find the path of a sensor directory that starts with 28
            devicelist = glob.glob('/sys/bus/w1/devices/28*')
            # append the device file name to get the absolute path of the sensor 
            devicefile = devicelist[0] + '/w1_slave'

            # open the file representing the sensor.
            fileobj = open(devicefile,'r')
            lines = fileobj.readlines()
            fileobj.close()

            # print the lines read from the sensor apart from the extra \n chars
            
            temperaturedata = lines[1].split(" ")[9] 
            # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
            temperature = float(temperaturedata[2:]) 
            # Put the decimal point in the right place and display it. 
            temperature = temperature / 1000 
            print temperature
            return temperature
def main1():
    app=TemperatureSensing()
    app.get_name()
    tempvalue=app.get_temperature()
    if(tempvalue > 26):
        test2.startProcess('1')    

if __name__ == '__main__':
    main1()
