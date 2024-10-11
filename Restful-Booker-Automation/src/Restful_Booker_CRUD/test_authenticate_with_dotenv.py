# PASSWORD -  store the password in the framewor?

# Env File - .(dot.env)
# How do you store your password or credentials in the framework.
# pip install python-dotenv


import pytest
from dotenv import load_dotenv
import os

def test_authenticate():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)


