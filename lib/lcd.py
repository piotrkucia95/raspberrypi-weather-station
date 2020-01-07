# -*- coding: UTF-8 -*-

import time
import RPi.GPIO as GPIO

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
LED_ON = 15

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

"""
def main():
  # Main program block

  # Initialise display
  lcd_init()

  # Toggle backlight on-off-on
  GPIO.output(LED_ON, True)
  time.sleep(1)
  GPIO.output(LED_ON, False)
  time.sleep(1)
  GPIO.output(LED_ON, True)
  time.sleep(1)
  
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
            # line = "PM 2.5: {} μg/m^3  PM 10: {} μg/m^3".format(pm_25, pm_10)
            # print(datetime.now().strftime("%d %b %Y %H:%M:%S.%f: ")+line)
            
            # Send some right justified text
            lcd_byte(LCD_LINE_1, LCD_CMD)
            lcd_string("Temperature:", 1)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string(str("{:.1f}".format(temperature)) + " " + chr(223) + "C",3)
    
            time.sleep(2)
    
            lcd_byte(LCD_LINE_1, LCD_CMD)
            lcd_string("Pressure:", 1)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string(str("{:.1f}".format(pressure)) + " hPa", 3)
    
            time.sleep(2)
    
            lcd_byte(LCD_LINE_1, LCD_CMD)
            lcd_string("Humidity:", 1)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string(str("{:.1f}".format(humidity)) + " %", 3)
    
            time.sleep(2)
    
            lcd_byte(LCD_LINE_1, LCD_CMD)
            lcd_string("PM 2,5:", 1)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string(str("{:.1f}".format(pm_25)) + " ug/m^3", 3)
    
            time.sleep(2)
    
            lcd_byte(LCD_LINE_1, LCD_CMD)
            lcd_string("PM 10:", 1)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            lcd_string(str("{:.1f}".format(pm_10)) + " ug/m^3", 3)
    
            time.sleep(2)
            
        cnt += 1
        if (cnt == 5):
            cnt = 0

  # Turn off backlight
  GPIO.output(LED_ON, False)
"""


def lcd_init():
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable  
  # Initialise display
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)  
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

def lcd_string(message,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified

  if style==1:
    message = message.ljust(LCD_WIDTH," ")  
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)      

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)   

if __name__ == '__main__':
  main()
