from flask import  Flask, render_template, request
import requests, json
import urllib.request



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ff92b3d023e9f89d954f4045d6e5b5c4c1f6704568ce9a1a'


# the view
@app.route('/',methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        pass
    else:
        city = request.args.get('city')
        CITY = city
        API_KEY = "YOUR API KEY" 
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
        response = requests.get(URL)
        if response.status_code == '404':
            error = 'City not found'
            return render_template('index.html', data=error)
        else:
            data = response.json()
            main = data['main']
            """getting all data needed from the block. temp, humidity etc"""
            temperature = round(main['temp'] - 273.15)
            temp_feel_like = main['feels_like']
            humidity = main['humidity']
            pressure = main['pressure']
            weather_report = data['weather']
            wind_report = data['wind']
             # store them results in dict
            result = {
                 'temperature': temperature,
                 'temp_feel_like':temp_feel_like,
                 'humidity':humidity,
                 'pressure':pressure,
                 'weather_report':weather_report,
                 'wind_report':wind_report
             }
            
            searched_city = CITY

        
            return render_template('index.html', data=result, cityname=searched_city)


if __name__ == '__main__':
    app.run(debug=True)

