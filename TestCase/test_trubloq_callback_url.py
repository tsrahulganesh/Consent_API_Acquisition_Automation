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
    #----Verify that the system allows DLT platform to send the consent acquisition status ""INITIATED"" to call back URL------------------------
    # ---------------------------------------mentioned in DLT portal.-------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_ACCEPTED_02():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows DLT platform to send the consent acquisition status "ACCEPTED" to call back URL mentioned in DLT portal.-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "ACCEPTED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_FAILED_03():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows DLT platform to send the consent acquisition status "FAILED" to call back URL mentioned in DLT portal.-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "FAILED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_REJECTED_04():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows DLT platform to send the consent acquisition status "REJECTED" to call back URL mentioned in DLT portal.-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "REJECTED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_INVALID_MSISDN_05():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "INVALID-MSISDN" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "INVALID-MSISDN"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_DUPLICATE_06():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "DUPLICATE" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "DUPLICATE"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_REVOKED_07():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "REVOKED" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "REVOKED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_MNP_EXPIRED_08():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "MNP-EXPIRED" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "MNP-EXPIRED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_EXPIRED_09():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "EXPIRED" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "EXPIRED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_status_DISCONNECTED_10():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system allows DLT platform to send the consent acquisition status "DISCONNECTED" to call back URL mentioned in DLT portal."-------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": "DISCONNECTED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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

    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_url_blank_MSISDN_11():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #----"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call back URL
    #---------mentioned in DLT portal for blank MSISDN"-----------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"msisdn": " "})
    input_json_dict["callback_url"][0].update({"status": "ACCEPTED"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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


def test_callback_url_blank_uts_18():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------Verify that the system sends callback url request to retry queue when DLT platform sends the consent-----------------------------------
    #-----------------------acquisition status to call back URL mentioned in DLT portal for blank uts--------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"uts": " "})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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


def test_callback_url_blank_source_19():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------Verify that the system sends callback url request to retry queue when DLT platform sends the consent-----------------------------------
    #-----------------------acquisition status to call back URL mentioned in DLT portal for blank source--------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"source": " "})
    request_json = json.dumps(input_json_dict["callback_url"][0])
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
