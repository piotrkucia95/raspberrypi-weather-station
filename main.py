import sensors
from lib import lcd
from flask import Flask, render_template

def main():
    
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/values')
    def values():
        values = sensors.get_values()
        return str(values)
    
    app.run(host='0.0.0.0')
    
    lcd.lcd_init()

    while True:  
        display_values(values)


def display_values(values):
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("Temperature:", 1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str("{:.1f}".format(values[0])) + " " + chr(223) + "C",3)

    time.sleep(2)

    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("Pressure:", 1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str("{:.1f}".format(values[1])) + " hPa", 3)

    time.sleep(2)

    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("Humidity:", 1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str("{:.1f}".format(values[2])) + " %", 3)

    time.sleep(2)

    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("PM 2,5:", 1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str("{:.1f}".format(values[3])) + " ug/m^3", 3)

    time.sleep(2)

    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("PM 10:", 1)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str("{:.1f}".format(values[4])) + " ug/m^3", 3)

    time.sleep(2)

if __name__ == '__main__':
  main()