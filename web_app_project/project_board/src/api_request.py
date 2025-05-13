import requests
import json
import os
from datetime import datetime
from . import parser
from . import data
from . import days

class Api_Request:
    """
    This class calls the openmeteo api.
    a call function to get latitude and longitutde that return json
    and another function to get the weather data itself that reuturns json
    two functions to save the request data into two files
    """
    def get_cords_data(self, location: str) -> dict:
        if type(location) != str:
            raise TypeError("location is not type str")

        x = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json')

        return x.json()

    def get_weather_data(self, lat, lon):
        if type(lat) != float or type(lon) != float:
            raise TypeError("lat or lon is not type int")

        x = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=relative_humidity_2m&daily=temperature_2m_max,temperature_2m_min')

        return x.json()

    def save_geocoding_respnse_in_file(self, data: dict) -> None:
        if type(data) != dict:
            raise TypeError("The data is not type dict")

        if os.path.exists("api_gecode_response.json"):
            with open("api_gecode_response.json", "r") as file:
                try:
                    data_list = json.load(file)
                except json.JSONDecodeError:
                    data_list = []
        else:
            data_list = []

        data_list.append(data)

        with open("api_gecode_response.json", "w") as file:
            json.dump(data_list, file)

    def save_data_respnse_in_file(self, data, city):
        if type(data) != dict:
            raise TypeError("The data is not type dict")

        directory = 'data_files'
        if not os.path.exists(directory):
            os.makedirs(directory)

        data_list = []
        data_list.append(data)

        file_name = directory + '/' + datetime.now().strftime("%Y-%m-%d") + '_' + city + '.json'
        print(file_name)
        with open(file_name, "w") as file:
            json.dump(data_list, file)


    
def main_def(name):
    """Main function where the calls to the Api class is made here, in this function the data get assigned to class objects too"""

    api = Api_Request()
    cords_jason = api.get_cords_data(name)
    api.save_geocoding_respnse_in_file(cords_jason)

    pars = parser.Parser()
    weather_data = data.Data()

    cords_result = pars.get_cords(cords_jason)

    lat = cords_result[0][0]['latitude']
    lon = cords_result[0][0]['longitude']

    weather_data.set_city(cords_result[0][0]['name'])
    weather_data.set_country(cords_result[0][0]['country'])

    weather_jason = api.get_weather_data(lat, lon)
    api.save_data_respnse_in_file(weather_jason, weather_data.get_city())

    week_result = pars.get_week(weather_jason)

    slice_min = 1
    slice_max = 25
    hours_in_day = 24
    days_in_week = 7
    for i in range(days_in_week):
        sum_day = week_result[slice_min:slice_max]
        slice_min = slice_max
        slice_max += hours_in_day
        
        weather_data.set_week(days.Daily())
        
        a = weather_data.get_day_by_index(i)
        a.set_date(week_result[0]['time'][i])
        a.set_day_temp(week_result[0]['temperature_2m_max'][i])
        a.set_night_temp(week_result[0]['temperature_2m_min'][i])
        a.set_humidity(sum(sum_day) / hours_in_day)
    return weather_data
