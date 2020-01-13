from weather import Weather
from server import Server

import threading, time, datetime

def main_loop():
    weather.init_lcd()
    latest_measure = server.get_latest_data(1)[0]
    
    while True:
        now = datetime.datetime.now()
        if (latest_measure[1].hour != now.hour):
            measure_time = now
            latest_measure = [1, measure_time, weather.temperature, weather.pressure, weather.humidity, weather.pm25, weather.pm10]
            server.save_to_db(latest_measure)
        
        server.set_weather(weather)
        weather.display_values()
        weather.get_values()

weather = Weather()  
server = Server()  
    
thread1 = threading.Thread(target = main_loop, args = ())
thread1.start()

server.run_server()





    
