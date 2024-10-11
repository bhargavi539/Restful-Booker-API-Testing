import pytest
import requests
import allure
@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=url, headers=headers,json=json_payload)
    token = response.json()["token"]
    print(token)
    return token




@pytest.fixture
def create_booking():
    url ="https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    print(type(url))
    print(type(headers))
    print(type(json_payload))

    response = requests.post(url=url,headers=headers,json=json_payload)
    booking_id = response.json()["bookingid"]
    return booking_id