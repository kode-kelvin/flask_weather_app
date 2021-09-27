import requests, json

CITY = input('enter city name:').upper() #ask user input
API_KEY = "494e02d29c6be05ea895dd671982ef04" # Your API key
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}" # URL
# Sending HTTP request
response = requests.get(URL)
if response.status_code == '404':
    print('City not found')
else:
    data = response.json()# retrieving data in the json format
    main = data['main']  # the main block
    temperature = round(main['temp'] - 273.15) # get'n temp - convert to celsius and round off
    temp_feel_like = main['feels_like']# get'n feel like
    humidity = main['humidity'] # get'n the humidity
    pressure = main['pressure']   # getting the pressure
    weather_report = data['weather'] # weather report
    wind_report = data['wind']    # wind report
    print(f"{CITY:*^40}")
    print(f"City ID: {data['id']}")   
    print(f"Temperature: {temperature}ºC")
    print(f"Feel Like: {temp_feel_like}")    
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {weather_report[0]['description']}")
    print(f"Wind Speed: {wind_report['speed']}")
    print(f"Time Zone: {data['timezone']}")

   