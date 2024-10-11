import allure # pip install allure
import pytest # pip install pytest
import requests # pip install requests


@allure.title("TC_01 - Create Booking")
@allure.description("Verify create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    #Payload / Data / Body - Dict / JSON
    # Auth(No)

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    response = requests.post(url=URL,headers=headers,json=payload)
    assert response.status_code == 200
    responseData = response.json()


    """
    Response body verification
    """
    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) is int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True


    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"



@allure.title("TC_02 - Create Booking negative")
@allure.description("Verify create booking by not sending any payload with post request")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}

    response = requests.post(url=URL,headers=headers,json=payload)
    assert response.status_code == 500


@allure.title("TC_03 - Create Booking negative")
@allure.description("Verify create booking with totalprice - string negative")
@pytest.mark.crud
def test_create_booking_negative_tc3(): # Bug Raise to client or Dev.
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload ={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : "string",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertions
    assert response.status_code == 200