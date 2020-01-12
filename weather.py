from lib import bme280, sds011, lcd
import time

class Weather: 
    def __init__(self):
        self.get_values()
    
    def get_values(self):
        temp, press, hum = bme280.readBME280All()
        pm25, pm10 = sds011.get_airquality()
        
        self.temperature = round(temp, 1)
        self.pressure = round(press, 1)
        self.humidity = round(hum, 1)
        self.pm25 = round(pm25, 1)
        self.pm10 = round(pm10, 1)  

    def init_lcd(self):
        lcd.lcd_init()
        
    def display_values(self):
        attrs = ['Temperature', 'Pressure', 'Humidity', 'PM25', 'PM10']
        values = [self.temperature, self.pressure, self.humidity, self.pm25, self.pm10]
        units = [chr(223) + 'C', 'hPa', '%', 'ug/m^3', 'ug/m^3']
        
        for x in range(5):
            lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
            lcd.lcd_string(attrs[x] + ':', 1)
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string(str("{:.1f}".format(values[x])) + " " + units[x], 3)
            
            time.sleep(2)       
            
            
