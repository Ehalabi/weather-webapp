import pytest
from project_board.src import data
from project_board.src.days import Daily

data = data.Data()

def test_set_city():
    city = "luxembourg"

    data.set_city(city)

    with pytest.raises(TypeError) as x:
        data.set_city(120.124)

    assert data.city == city
    assert str(x.value) == "city is not of type str"

def test_set_country():
    country = "luxembourg"

    data.set_country(country)

    with pytest.raises(TypeError) as x:
        data.set_country(1)

    assert data.country == country
    assert str(x.value) == "country is not of type str"


def test_set_week():
    obj1 = Daily()
    obj2 = Daily()
    
    data.set_week(obj1)
    data.set_week(obj2)
    
    assert data.get_day_by_index(0) == obj1
    assert data.get_day_by_index(1) == obj2



