class Daily:
    """
    Daily class has attributes on the weather on one single day.
    Has attributes date, the daily temprature, the night temprature,
    and humidity.
    Has four functions that is used to set those attributes.
    """
    def __init__(self):
        self.date = None
        self.day_temp = None
        self.night_temp = None
        self.humidity = None

    def set_date(self,date_var: str) -> None:
        if type(date_var) != str:
            raise TypeError("date_var type is not str")
        self.date = date_var

    def set_day_temp(self, day_temp: float) -> None:
        if type(day_temp) not in (float, int):
            raise TypeError("day_temp type is not float or int")
        self.day_temp = day_temp

    def set_night_temp(self, night_temp: float) -> None:
        if type(night_temp) not in (float, int):
            raise TypeError("night_temp type is not float or int")
        self.night_temp = night_temp

    def set_humidity(self, humidity: (float, int)) -> None:
        """We set humidity to be int, it's received type will be float but can be int depending on the api"""
        if type(humidity) not in (float, int):
            raise TypeError("humidity type is not float or int")
        self.humidity = int(humidity)

