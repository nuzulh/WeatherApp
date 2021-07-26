import requests
from datetime import datetime

api_key = 'c36bc2fd7ce762a4707aa43361293b98'
location = input("Enter the city name: ")

complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print (f"Weather Stats for - {location.upper()}  || {date_time}")
print ("-------------------------------------------------------------")

print (f"Current temperature is: {temp_city:.2f} deg C")
print (f"Current weather desc  : {weather_desc}")
print (f"Current Humidity      : {hmdt} %")
print (f"Current wind speed    : {wind_spd} kmph")

print("====================================================")

txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]

with open("textfile.txt" , mode='w' ,encoding='utf-8') as f:

    f.write("------------------------------------------------------------- \n ")   
    f.write(f"Weather Stats for - {location.upper()}  || {date_time}")
    f.write("\n------------------------------------------------------------- \n")
    f.write(f"Current temperature is: {txtlist[0]:.2f} deg C\n")
    
    f.write(f"\nCurrent weather desc  : {txtlist[1]}")
    f.write(f"\nCurrent Humidity      : {txtlist[2]} %")
    f.write(f"\nCurrent wind speed    : {txtlist[3]} kmph")
    f.write("\n====================================================")
    

    
