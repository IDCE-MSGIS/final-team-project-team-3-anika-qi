'''
# Assignment title: Final Project- Web-scrape Script 1
# Date: 10/02/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
#Time Spent: 20 minutes 
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []
## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
# Enter the lat&lon 
lat = input('Please enter the latitude: ')
lon = input('Please enter the longitude: ')

# Change the type of lat&lon.
lat=str(lat)
lon=str(lon)

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
#replace the wrong words
for day in forecast:
    day = day.replace('N', ' N')
    day = day.replace('Low', ', Low')
    day = day.replace('High', ', High')
    day = day.replace('C', ' C')
    day = day.replace('A', ' A')
    day = day.replace('P', ' P')
    day = day.replace('S', ' S')
    day = day.replace('M', ' M')
    day = day.replace('H', ' H')
    day = day.replace('thenMostly', 'Then Mostly')
    day = day.replace('Likelythen', 'Likely Then')
    day = day.replace('\n\n ', '\n\n')
    day = day.replace('  ', ' ')
    # Capitalize all letters。
    day = day.upper()
    print day

