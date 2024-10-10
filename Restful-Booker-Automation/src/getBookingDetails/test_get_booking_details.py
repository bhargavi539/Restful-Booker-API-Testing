import allure
import pytest
import requests

@allure.title("Get Booking")
@allure.description("This test attempts to get existing booking details using a valid booking id. Fails if any error happens.")
@allure.tag("smoke")
@allure.severity("Critical")
@allure.testcase("TC_01")
@pytest.mark.smoke
def test_get_booking_by_valid_id():
    url = "https://restful-booker.herokuapp.com/booking/3"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200



@allure.title("Get Booking")
@allure.description("This test attempts to get booking details using a non existing booking id. It should return 404 status code.")
@allure.tag("smoke")
@allure.severity("Major")
@allure.testcase("TC_02")
@pytest.mark.smoke
def test_get_booking_by_non_existing_id():
    url = "https://restful-booker.herokuapp.com/booking/10997"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 404



@allure.title("Get Booking")
@allure.description("This test attempts to get existing booking details using a null booking id. It should return 404 status code.")
@allure.tag("smoke")
@allure.severity("Critical")
@allure.testcase("TC_03")
@pytest.mark.smoke
def test_get_booking_by_null_id():
    url = "https://restful-booker.herokuapp.com/booking/null"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 404



@allure.title("Get Booking")
@allure.description("This test attempts to get booking details using an already deleted booking id. It should return 404 status code.")
@allure.tag("smoke")
@allure.severity("Major")
@allure.testcase("TC_04")
@pytest.mark.smoke
def test_get_booking_by_already_deleted_id():
    url = "https://restful-booker.herokuapp.com/booking/898"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 404


@allure.title("Get Booking")
@allure.description("This test attempts to get booking details using a string. Fails if any error happens.")
@allure.tag("smoke")
@allure.severity("Critical")
@allure.testcase("TC_05")
@pytest.mark.smoke
def test_get_booking_by_string():
    url = "https://restful-booker.herokuapp.com/booking/emily"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 404