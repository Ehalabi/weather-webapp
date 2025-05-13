import pytest
from project_board.src import days

day_data = days.Daily()

def test_set_date():
    """This function tests the set date method."""
    date = "2010-07-15"

    day_data.set_date(date)

    with pytest.raises(TypeError) as x:
        day_data.set_date(12)


    assert str(x.value) == "date_var type is not str"
    assert day_data.date == date, "error in setting up date in Daily class"


def test_set_day_temprature():
    """This function tests the set day method."""
    day_temp = 40
    
    day_data.set_day_temp(day_temp)

    with pytest.raises(TypeError) as x:
        day_data.set_day_temp("string")

    assert str(x.value) == "day_temp type is not float or int"
    assert day_data.day_temp == day_temp


def test_set_night_temprature():
    """This function tests the set night method."""
    night_temp = -10

    day_data.set_night_temp(night_temp)

    with pytest.raises(TypeError) as x:
        day_data.set_night_temp("string")

    assert str(x.value) == "night_temp type is not float or int"
    assert day_data.night_temp == night_temp


def test_set_humidity():
    """This function tests the set humidity method."""
    humidity = 10.3

    day_data.set_humidity(humidity)

    with pytest.raises(TypeError) as x:
        day_data.set_humidity("1")

    assert str(x.value) == "humidity type is not float or int"
    assert day_data.humidity == int(humidity)
