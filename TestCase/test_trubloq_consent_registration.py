import datetime
from random import random
import requests
import json
import jsonpath
import os, time, re
from TestCase import test_modules
from TestCase.test_modules import *

def get_endpoint_consent_registration():
    endpoint_json = get_json_from_file("Config", "endpoints.json")
    create_consent_add_endpoint = json.loads(endpoint_json)["consent_registration"]
    return create_consent_add_endpoint


def test_register_consent_for_MSISDN_01():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that system allows user to register a consent for a MSISDN-------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
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

def test_providing_blank_MSISDN_02():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing blank MSISDN"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["msisdn"] = " "
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 508
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_providing_blank_entityid_03():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing blank entityid"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["entityid"] = " "
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
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

def test_providing_blank_constempid_04():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing blank constempid"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["constempid"] = " "
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
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

def test_providing_blank_source_05():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing blank source"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["source"] = " "
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
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

def test_providing_invalid_MSISDN_06():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing invalid MSISDN (size less than or more than 10 Chars)"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["msisdn"] = "78876949469"
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 508
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_providing_invalid_MSISDN_starwith_91_07():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing invalid MSISDN (MSISDN starting with "91")"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0]["msisdn"] = "9187694946"
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 508
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

