"""
Integrated scenario where we create a booking, update it and delete the booking by using
a token that is generated using create tokenAPI
"""

import allure
import pytest
import requests
from requests import delete


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
    assert response.status_code == 200

    booking_id = response.json()["bookingid"]
    return booking_id




def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    put_url = base_url + base_path

    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Accept" : "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Emily",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=put_url,headers=headers,json=json_payload)
    assert response.status_code == 200

    response_data = response.json()
    firstname = response_data["firstname"]
    assert firstname == "Emily"



def test_delete_booking():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    delete_url = url + str(booking_id)
    cookie = "token=" + create_token()
    headers = {
        "Content - Type": "application/json",
        "Cookie" : cookie
    }
    response = requests.delete(url=delete_url,headers=headers)
    assert response.status_code == 201













