import datetime
from random import random
import requests
import json
import jsonpath
import os, time, re
from TestCase import test_modules
from TestCase.test_modules import *


def get_endpoint_refresh_token():
    endpoint_json = get_json_from_file("Config", "endpoints.json")
    create_consent_add_endpoint = json.loads(endpoint_json)["generate_refresh_token"]
    return create_consent_add_endpoint

def test_gen_new_access_tok_providing_valid_refresh_token_01():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that the system allows user to generate a new access token by providing valid refresh token that was received in
    #-----Authorization Token API response json.---------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_refresh_token.json"))
    request_json = json.dumps(input_json_dict["api_refresh_token"][0])
    response = post_call(get_endpoint_refresh_token(), request_json, get_headers_without_Authorization())
    print("##url##", get_endpoint_refresh_token())
    print("#request#", request_json)
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 200

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

    # # Assert Mandatory Field level validation errors
    validate_field_mandatory_error(response_json, "access")

def test_providing_invalid_expire_token_02():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that the system returns error status with message for providing an invalid or expired refresh token in payload."----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_refresh_token.json"))
    input_json_dict["api_refresh_token"][0]["refresh"] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaC IsImV4cCI6MTU0ODM5MzU5NCwianRpIjoiYjFlZGFjYzE3ZTcxNGIwYmIyMzJkYzRlM2ZmYzFiNjM iLCJ1aWQiOjk1fQ.GrUjW4shdeQHk4rKhK19kPs5bedX3baaAt1UgeuEtTo"
    request_json = json.dumps(input_json_dict["api_refresh_token"][0])
    response = post_call(get_endpoint_refresh_token(), request_json, get_headers_without_Authorization())
    print("##url##", get_endpoint_refresh_token())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 401
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid Token or token expired"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_providing_blank_refresh_token_03():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that the system returns error status with message for providing a blank refresh token in payload."----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "generate_refresh_token.json"))
    input_json_dict["api_refresh_token"][0]["refresh"] = " "
    request_json = json.dumps(input_json_dict["api_refresh_token"][0])
    response = post_call(get_endpoint_refresh_token(), request_json, get_headers_without_Authorization())
    print("##url##", get_endpoint_refresh_token())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
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