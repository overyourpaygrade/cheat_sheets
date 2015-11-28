#! python3
#quickWeather.py - Prints the weater for a location from the command line

import json, requests, sys

# Compute the location from command line arguments
if len(sys.argv) < 2:
  print('Usage: quickWeather.py location')
  sys.exit()
location = ' ' .join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
# The requests.get() call returns a Response object, which you can check
# for errors by calling raise_for_status(). If no exception is raised
# the downloaded text will be in response.text

# Load JSON data and Print Weather
weatherData = json.loads(response.text)

# Print weater descriptions
w = weatherData['list']

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])