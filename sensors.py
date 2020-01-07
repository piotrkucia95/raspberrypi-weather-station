# -*- coding: UTF-8 -*-

from lib import bme280
import serial, time, struct, array

def get_values():
    ser = serial.Serial()
    ser.port = "/dev/ttyUSB0" # Set this to your serial port
    ser.baudrate = 9600

    ser.open()
    ser.flushInput()

    byte, lastbyte = "\x00", "\x00"
    cnt = 0
    
    while True:  
        temperature,pressure,humidity = bme280.readBME280All()
        
        lastbyte = byte
        byte = ser.read(size=1)
        
        if lastbyte == "\xAA" and byte == "\xC0":
            sentence = ser.read(size=8)
            readings = struct.unpack('<hhxxcc',sentence)

            pm_25 = readings[0]/10.0
            pm_10 = readings[1]/10.0
            
            if (cnt == 0 ):
                return [temperature, pressure, humidity, pm_25, pm_10];
                
            cnt += 1
            if (cnt == 5):
                cnt = 0