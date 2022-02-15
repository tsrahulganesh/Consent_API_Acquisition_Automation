import datetime
from random import random
import requests
import json
import jsonpath
import os, time, re
from TestCase import test_modules
from TestCase.test_modules import *

def get_endpoint():
    endpoint_json = get_json_from_file("Config", "endpoints.json")
    create_consent_add_endpoint = json.loads(endpoint_json)["generate_token"]
    return create_consent_add_endpoint

# DEMO_CONSENT_ADD_TC01

def test_gen_tok_valid_cred_01():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows user to generate access token and refresh token for provided valid username (DLT Entity ID of account)
    #------and valid password (generated on Telco portal for consent acquisition API)-------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    request_json = json.dumps(input_json_dict["api_token"][0])

    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 200

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

    # Assert Mandatory Field level validation errors
    validate_field_mandatory_error(response_json, "refresh")
    validate_field_mandatory_error(response_json, "access")
    # validate_field_mandatory_error(response_json, "ruleName")
    # validate_field_mandatory_error(response_json, "subAccount")
    # validate_field_mandatory_error(response_json, "sourceType")
    # validate_field_mandatory_error(response_json, "host")
    # validate_field_mandatory_error(response_json, "port")
    # validate_field_mandatory_error(response_json, "username")
    # validate_field_mandatory_error(response_json, "password")
    # validate_field_mandatory_error(response_json, "sourceDirectory")
    # validate_field_mandatory_error(response_json, "columnMapping")
    # validate_field_mandatory_error(response_json, "whenToProcessFile")
    # validate_field_mandatory_error(response_json, "destinationFolder")
    # validate_field_mandatory_error(response_json, "isAlert")
    # validate_field_mandatory_error(response_json, "subAccountPassword")
    #

def test_invalid_cred_02():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for an invalid username (DLT Entity ID of account) and invalid password--
    #--------(generated on Telco portal for consent acquisition API) for which no user is found----------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    input_json_dict["api_token"][0].update({"username": "1101635530000002261"})
    input_json_dict["api_token"][0].update({"password": "mpCN3MafV$Nqob"})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 504
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid login credentials"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_invali_username_valid_psw_03():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for a invalid username (DLT Entity ID of account) and valid password
    #--------(generated on Telco portal for consent acquisition API)----------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    input_json_dict["api_token"][0].update({"username": "1101635530000002261"})
    input_json_dict["api_token"][0].update({"password": "mpCN3MafV$NqoK"})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_blank_username_valid_psw_04():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for an username (DLT Entity ID of account)-------------------
    #---- sent as blank value and valid password (generated on Telco portal for consent acquisition API)------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    input_json_dict["api_token"][0].update({"username": " "})
    input_json_dict["api_token"][0].update({"password": "mpCN3MafV$NqoK"})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_valid_username_invalid_psw_05():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for a valid username (DLT Entity ID of account) and invalid password
    #-----(generated on Telco portal for consent acquisition API)------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    input_json_dict["api_token"][0].update({"username": "1101635530000002262"})
    input_json_dict["api_token"][0].update({"password": "mpCN3MafV$Nqoa"})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_valid_username_blank_psw_06():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for a valid username (DLT Entity ID of account) and blank password
    #----(generated on Telco portal for consent acquisition API)------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    input_json_dict["api_token"][0].update({"username": "1101635530000002262"})
    input_json_dict["api_token"][0].update({"password": " "})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_valid_username_psw_inactive_dlt_acc_07():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for a provided username and password of an inactive DLT account.------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    # input_json_dict["api_token"][0].update({"username": "1101635530000002262"})
    # input_json_dict["api_token"][0].update({"password": " "})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 503
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Peid not active"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_valid_username_psw_consent_api_not_enable_08():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for a provided username and password of a DLT account----------
    #----- for which Consent API is not enabled.------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    # input_json_dict["api_token"][0].update({"username": "1101635530000002262"})
    # input_json_dict["api_token"][0].update({"password": " "})
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 510
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] ==  "Consent API is not enabled for this account"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_only_valid_username_09():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that the system returns error status with message for providing only username parameter in payload.------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    del input_json_dict["api_token"][0]["password"]
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("####request####", json.dumps(input_json_dict["api_token"][0]))
    print("###response####", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 502
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Parameter is missing"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_only_valid_psw_10():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that the system returns error status with message for providing only password parameter in payload."------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_token.json"))
    del input_json_dict["api_token"][0]["username"]
    request_json = json.dumps(input_json_dict["api_token"][0])
    response = post_call(get_endpoint(), request_json, get_headers_without_Authorization())
    print("####request####", json.dumps(input_json_dict["api_token"][0]))
    print("###response####", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 502
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Parameter is missing"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

