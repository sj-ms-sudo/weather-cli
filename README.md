# 🌀 Weather CLI App

A simple Python CLI tool to get the current weather or a multi-day forecast using [WeatherAPI](https://www.weatherapi.com/).

## 🛠 Features

- 📍 Current weather
- 📅 1–14 day forecast
- 🌡 Metric or Imperial units
- 🌦 Chance of rain, sunrise/sunset, moon phase

## 🧪 Usage

```bash
# Current weather (default metric)
python weatherforecast.py -c Kochi

# 3-day forecast in imperial units
python weatherforecast.py -c "New York" --unit imperial --days 3
