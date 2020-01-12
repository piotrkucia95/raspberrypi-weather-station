from flask import Flask, render_template
import mysql.connector

class Server:
    def __init__(self):
        self.weather_db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='raspberry',
            database='weather'
        )
        self.db_cursor = self.weather_db.cursor()    
        self.app = Flask(__name__)
        self.set_routes()
           
    def set_weather(self, weather_obj):
        self.weather = weather_obj
           
    def set_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html', temperature=self.weather.temperature,
                                                 pressure=self.weather.pressure,
                                                 humidity=self.weather.humidity,
                                                 pm25=self.weather.pm25,
                                                 pm10=self.weather.pm10)
            
        @self.app.route('/history/<number_of_rows>')
        def history(number_of_rows):
            results = self.get_latest_data(number_of_rows)          
            return render_template('history.html', results=results)
    
    def run_server(self):
        self.app.run('0.0.0.0')
        
    def get_latest_data(self, number_of_rows):
        self.db_cursor.execute("SELECT * FROM `weather-data` ORDER BY date DESC LIMIT %s" % number_of_rows)
        return self.db_cursor.fetchall()
    
    def save_to_db(self, data):
        query = """INSERT INTO `weather-data` (`date`, `temperature`, `pressure`, `humidity`, `pm25`, `pm10`)
                   VALUES (%s, %s, %s, %s, %s, %s) """
        recordTuple = (data[1], data[2], data[3], data[4], data[5], data[6])
        self.db_cursor.execute(query, recordTuple);
        self.weather_db.commit()
        
        
        
        
        
        
        
