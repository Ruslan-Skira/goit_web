import requests
from unittest.mock import Mock, patch

def send_request(url:str) -> int:
    response = requests.get(url)
    return response.status_code


def test_send_request():
    mock_get = Mock(return_value=Mock(status_code=200))
    with patch('requests.get', mock_get):
        status_code = send_request("https://docs.python.org/3/library/unittest.mock-examples.html")
        assert  status_code == 200  # first check
        mock_get.assert_called_once_with("https://docs.python.org/3/library/unittest.mock-examples.html") # second check


mock_get = Mock(return_value=Mock(status_code=200))


@patch('requests.get', mock_get)
def test_send_request():
    send_request("https://docs.python.org/3/library/unittest.mock-examples.html")
    send_request("https://docs.python.org/3/library/unittest.mock-examples.html")
    mock_get.assert_called_once_with("https://docs.python.org/3/library/unittest.mock-examples.html") # second check