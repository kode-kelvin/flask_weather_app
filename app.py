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
        API_KEY = "30d4741c779ba94c470ca1f63045390a" # Your API key
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
        response = requests.get(URL)
        if response.status_code == '404':
            error = 'City not found'
            return render_template('index.html', data=error)
        else:
            data = response.json()# retrieving data in the json format
            main = data['main']  # the main block from api block
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

      
"""
Option 2

@app.route('/', methods =['POST', 'GET'])
def weather():
   if request.method == 'POST':
       city = request.form['city']
   else:
       # for default name mathura
       city = 'mathura'
   # your API key will come here
   api = "30d4741c779ba94c470ca1f63045390a"
   source = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}").read()
   list_of_data = json.loads(source) #json to data convert
   # data for variable list_of_data
   data = {
       "country_code": str(list_of_data['sys']['country']),
       "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                   + str(list_of_data['coord']['lat']),
       "temp": str(list_of_data['main']['temp']) + 'k',
       "pressure": str(list_of_data['main']['pressure']),
       "humidity": str(list_of_data['main']['humidity']),
   }
   print(data)
    return render_template('weather.html', data = data)
"""


if __name__ == '__main__':
    app.run(debug=True)

