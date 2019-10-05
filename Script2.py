# Users enter longitude and latitude to get weather information and dressing advice for recent days
# Place necessary comments and code here. 

# import required libraries
import requests
import re
from bs4 import BeautifulSoup

# List to store response
forecast = []

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

# weather function
str1=''
def advice(temp):
  if temp >= 100:
    str1 = "It is hot. \n We recommend you to wear T-shirts, shorts and skirts.\n Be careful not to have heat stroke!"
  elif temp >= 70 and temp < 100:
    str1 = "It is warm.\n We recommend you to wear shirts, shorts and skirts. "
  elif temp >= 32 and temp < 70:
    str1= "It is cool.\n We recommend you to wear hoodies, coat, sweater and pants\n Be careful not to catch a cold!"
  else:
    str1 = "It is cold.\n We recommend you to wear sweater, down jacket and cotton coat.\n keep warm!"
  return str1


# Extracting numbers
number=[]
for i in forecast:
  r= re.findall(r'\d+\.?\d*',i)
  number.append(int(r[0])) 

# Print list to remove unicode characters
#replace the wrong words

x=0
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
    # Capitalize all letters.
    day = day.upper()
    print day 
    # use the function to output advice
    temp = int(number[x])
    print advice(temp)
    x=x+1
    
