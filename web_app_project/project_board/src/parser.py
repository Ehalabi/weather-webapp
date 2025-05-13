class Parser:
    """
    A class that has two function that get json data of type dict
    and parses through it, returns only what is needed and the actual
    data assingment is done in the api_request model
    """

    def get_cords(self, json: dict) -> list:
        if type(json) != dict:
            raise TypeError("Json is not type dict")

        return [json['results']]

    def get_week(self,json: dict) -> list:
        if type(json) != dict:
            raise TypeError("Json is not type dict")

        days_list = [json['daily']]
        humidity = json['hourly']['relative_humidity_2m']

        return days_list + humidity
