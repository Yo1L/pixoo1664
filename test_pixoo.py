from pixoo1664 import Pixoo, InvalidPixooResponse
import pytest


def test_fail_to_load_counter(mocker):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    mock_get_response = mocker.Mock(status_code=200)
    mock_get_response.json.return_value = {"error_code": 1}
    mocker.patch("requests.post", return_value=mock_get_response)

    try:
        Pixoo("1.1.1.1")
    except InvalidPixooResponse as ex:
        assert ex != None


def test_fail_to_connect(mocker):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    mocker.patch("requests.post", status_code=500)

    try:
        Pixoo("1.1.1.1")
    except InvalidPixooResponse as ex:
        assert ex != None


def test_to_load_counter(mocker):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    mock_get_response = mocker.Mock(status_code=200)
    mock_get_response.json.return_value = {"error_code": 0, "PicId": 0}
    mocker.patch("requests.post", return_value=mock_get_response)

    try:
        Pixoo("1.1.1.1")
    except Exception as ex:
        pytest.fail(ex)


def test_set_brightness(mocker):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""
    mock_response = mocker.Mock(status_code=200)
    mock_response.json.return_value = {"error_code": 0}
    mocker.patch("requests.post", return_value=mock_response)

    try:
        pixoo = Pixoo("1.1.1.1", auto_load_counter=False)

        pixoo.set_brightness(10)
    except Exception as ex:
        pytest.fail(ex)


def test_disable_exceptions(mocker):
    """Given a city name, test that a HTML report about the weather is generated
    correctly."""

    try:
        pixoo = Pixoo("1.1.1.1", raise_exceptions=False, auto_load_counter=False)
        assert pixoo.set_screen(True) == False
    except InvalidPixooResponse as ex:
        pytest.fail("ouch")
