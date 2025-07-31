import argparse
import requests
import json
def currentforecast(api_key,city,unit):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    try:
        location = data["location"]
    except:
        print(f"Location {city} not found ! \n Please try again")
        exit()
    current = data["current"]
    text = current["condition"]["text"]
    temp_c = current["temp_c"]
    temp_f = current["temp_f"]
    wind_mph = current["wind_mph"]
    wind_kph = current["wind_kph"]
    wind_dir = current["wind_dir"]
    precip_mm=current["precip_mm"]
    precip_in=current["precip_in"]
    humidity=current["humidity"]
    cloud = current ["cloud"]
    feelslike_c=current["feelslike_c"]
    feelslike_f=current["feelslike_c"]
    vis_km=current["vis_km"]
    vis_miles=current["vis_km"]
    uv=current["uv"]
    if unit =="metric":
        print(f"The current weather at {city}")
        print(f'Temperature: {temp_c} degree celcius')
        print(f'{text}')
        dir = {"N":"North","NE":"North East","E":"East","SE":"South East","S":"South","SW":"South West","W":"West","NW":"North West"}
        print(f'Wind speed :{wind_kph}kph in direction {dir[wind_dir]}')
        print(f'Precipitation : {precip_mm} mm')
        print(f'Humidity : {humidity}')
        print(f'Cloud : {cloud}')
        print(f'Temperature feels like {feelslike_c} degree celcius')
        print(f'Visibility : {vis_km} km')
        print(f'UV index : {uv}')
    if unit =="imperial":
        print(f"The current weather at {city}")
        print(f'Temperature: {temp_f} degree fahrnheit')
        print(f'{text}')
        dir = {"N":"North","NE":"North East","E":"East","SE":"South East","S":"South","SW":"South West","W":"West","NW":"North West"}
        print(f'Wind speed :{wind_mph}mph in direction {dir[wind_dir]}')
        print(f'Precipitation : {precip_in} inches')
        print(f'Humidity : {humidity}')
        print(f'Cloud : {cloud}')
        print(f'Temperature feels like {feelslike_f} degree fahrnheit')
        print(f'Visibility : {vis_miles} miles')
        print(f'UV index : {uv}')
def forecastDays(api_key,city,unit,days):
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}'
    response = requests.get(url)
    data = response.json()
    try:
        location = data["location"]
    except:
        print(f"Location {city} not found ! \n Please try again")
        exit()
    print(f"{days} forecast in {city}")
    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        condition = day["day"]["condition"]["text"]
        max_temp_c = day["day"]["maxtemp_c"]
        min_temp_c = day["day"]["mintemp_c"]
        max_temp_f = day["day"]["maxtemp_f"]
        min_temp_f = day["day"]["mintemp_f"]
        chance_of_rain=day["day"]["daily_chance_of_rain"]
        sunrise=day["astro"]["sunrise"]
        sunset = day["astro"]["sunset"]
        moon_phase=day["astro"]["moon_phase"]
        print(f"{date}")
        print(f"Weather : {condition}")
        if unit == "metric":
            print(f"Temperature : {min_temp_c} degree celcius - {max_temp_c} degree celcius")
        else:
            print(f"Temperature : {min_temp_f} degree fahrnheit - {max_temp_f} degree fahrnheit")
        print(f"Chance of Rain : {chance_of_rain}%")
        print(f"Sunrise : {sunrise}")
        print(f"Sunset : {sunset}")
        print()

if __name__ == "__main__":
    api_key = "545530b2adee4ad5a82121909253107"
    parser = argparse.ArgumentParser(description = "python weatherforecast.py -c <cityname> --unit")
    parser.add_argument("-c","--cityname",help = "Enter the city name")
    parser.add_argument("--unit",default="metric",help = "Leave if wanter metric system or <imperial> is imperial system is needed")
    parser.add_argument("--days",type = int, help ="The number of days to forecast , leave if current weather is needed")
    args = parser.parse_args()
    city = args.cityname
    unit = args.unit
    if args.days:
        forecastDays(api_key,city,unit,args.days)
    else:
        currentforecast(api_key,city,unit)