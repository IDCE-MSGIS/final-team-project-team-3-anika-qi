import urllib.request
import gzip
import json
import sys
import urllib
import urllib.request

# code from PYQT

#gain weather
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.examples.activeqt.webbrowser.ui_mainwindow import Ui_MainWindow
from PyQt5.uic.properties import QtGui, QtWidgets, QtCore
from pip._vendor import requests


class mywindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.input_button.clicked.connect(self.get_weather_data) #click to start


    # function to gain weather
    def get_weather_data(self):
        # get city name
        city = self.cityname.text()
        # use api
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=1a8d31cac550511d792284d7d0f7dd5d&q='
        # gain url

        url = api_address + urllib.parse.quote(city)
        json_data = requests.get(url).json()
        # request and gain weather_data.
        # Storing single value in local variables, so that we can use later on.
        city_name = json_data['name']
        country_name = json_data['sys']['country']
        condition = json_data['weather'][0]['main']
        temp = json_data['main']['temp']
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        min_temp = json_data['main']['temp_min']
        max_temp = json_data['main']['temp_max']
        visibility = json_data['visibility']
        wind_speed = json_data['wind']['speed']
        wind_deg = json_data['wind']['deg']
        # print today weather
        self.textBrowser.setText(
            'Location: ' + city_name + country_name + '\n'
            'Condition : ' + condition + '\n'
            'Temperature : ' + temp + '\n'
            'Pressure : ' + pressure + '\n'
            'Humidity : ' + humidity + '\n'
            'Min. temperature : ' + min_temp + '\n'
            'Max. temperature : ' + max_temp + '\n'
            'Visibility : ' + visibility + '\n'
            'Wind speed : '+ wind_speed + ' per Km' + '\n'
            'Wind deg : ' + wind_deg + '\n')
        # create a string to put advice .
        str1 = ''
        # Recommend for dressing according by temperature.
        if temp >= 100:
            str1 = "It is hot. \n We recommend you to wear T-shirts, shorts and skirts.\n Be careful not to have heat stroke!\n"
        elif temp >= 70:
            str1 = "It is warm.\n We recommend you to wear shirts, shorts and skirts.\n "
        elif temp >= 32:
            str1= "It is cool.\n We recommend you to wear hoodies, coat, sweater and pants\n Be careful not to catch a cold!\n"
        else:
            str1 = "It is cold.\n We recommend you to wear sweater, down jacket and cotton coat.\n keep warm!\n"
        # print advice
        self.textBrowser_2.setText2(str)

if __name__ == "__main__":
            app = QApplication(sys.argv)
            win = mywindow()
            win.show()
            sys.exit(app.exec())




