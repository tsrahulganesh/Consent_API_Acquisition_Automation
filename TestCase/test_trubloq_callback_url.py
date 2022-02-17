import datetime
from random import random
import requests
import json
import jsonpath
import os, time, re
from TestCase import test_modules
from TestCase.test_modules import *

def get_endpoint_callback_url():
    endpoint_json = get_json_from_file("Config", "endpoints.json")
    create_callback_url_endpoint = json.loads(endpoint_json)["callback_url"]
    return create_callback_url_endpoint


def test_callback_url_status_initiated_01():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows DLT platform to send the consent acquisition status "ACCEPTED" to call back URL------------------------
    # ---------------------------------------mentioned in DLT portal.-------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "Success"

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))


