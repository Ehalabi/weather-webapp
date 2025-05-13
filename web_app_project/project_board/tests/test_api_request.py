import pytest
from project_board.src import api_request

api = api_request.Api_Request()

def test_get_cords_mocked(mocker):
    mock_data = {
            "results":
             [{"id":294801,
               "name":"Haifa",
               "latitude":32.81841,
               "longitude":34.9885,"elevation":40.0,
               "feature_code":"PPLA","country_code":"IL",
               "admin1_id":294800,"timezone":"Asia/Jerusalem",
               "population":267300,
               "country_id":294640,
               "country":"Israel",
               "admin1":"Haifa"}],
             "generationtime_ms":0.7659197
             }

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data

    mocker.patch("requests.get", return_value=mock_response)

    result = api.get_cords_data("Haifa")

    with pytest.raises(TypeError) as x:
            api.get_cords_data(120)

    assert result == mock_data
    assert type(result) is dict
    assert result['results'][0]['country'] == "Israel"
    assert str(x.value) == "location is not type str"

def test_get_weather_data(mocker):
    mock_data = [{"time":["2025-01-22","2025-01-23","2025-01-24","2025-01-25","2025-01-26","2025-01-27","2025-01-28"],"temperature_2m_max":[18.5,16.8,17.1,18.4,18.3,18.2,17.9],"temperature_2m_min":[14.3,12.7,11.6,11.4,12.2,8.9,8.8]}] + [40,40,39,38,38,38,39,38,37,36,36,35,35,37,40,43,49,53,57,60,69,74,83,86,87,90,92,92,91,91,88,84,81,81,76,76,79,81,85,85,86,87,88,88,88,88,87,88,90,92,93,94,94,93,89,79,69,62,64,71,71,74,75,77,78,78,79,81,90,93,93,93,93,93,92,90,91,88,76,64,50,42,44,51,57,60,63,66,69,73,74,72,68,66,66,68,69,70,71,72,73,73,72,68,63,60,60,62,65,70,77,82,86,89,90,90,88,86,83,80,78,93,92,91,91,91,87,77,63,52,44,39,38,43,52,61,70,80,85,84,79,74,71,69,68,69,70,71,71,71,69,63,55,48,44,42,42,44,47,51,57,64,68,69,67,65,64,62]

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = mock_data

    mocker.patch("requests.get", return_value=mock_response)

    result = api.get_weather_data(32.81841, 34.9885)

    with pytest.raises(TypeError) as x:
        api.get_weather_data("w", 1.1)

    assert result == mock_data
    assert result[0]['time'][0] == "2025-01-22"
    assert str(x.value) == "lat or lon is not type int"
