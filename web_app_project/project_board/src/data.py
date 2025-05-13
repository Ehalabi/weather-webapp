class Data:
    """
    Data class for the data of seven days.
    has 3 attributes, the city's name, the country's name, and a list called week
    that should hold objects of type Daily.
    There are 3 functions to set the class attributes and one function to return
    an object from the list week at a specific index
    """
    def __init__(self):
        self.city = None
        self.country = None
        self.week = []

    def set_city(self, city: str) -> None:
        if type(city) != str:
            raise TypeError("city is not of type str")
        self.city = city

    def set_country(self, country: str) -> None:
        if type(country) != str:
            raise TypeError("country is not of type str")
        self.country = country

    def set_week(self, obj) -> None:
        """Gets an object of type Daily from days.py and appends it into a list."""
        self.week.append(obj)

    def get_day_by_index(self, index: int) -> None:
        if type(index) != int:
            raise TypeError("index is not of type int")
        return self.week[index]

    def get_city(self):
        return self.city
