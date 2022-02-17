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

def test_consent_req_invalid_msisdn_08():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----Verify that system returns error status with message for providing invalid MSISDN (MSISDN not starting with '6/7/8/9')--------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0].update({"msisdn": "2887694946"})
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("#######", response.text)
    # Validate Response code
    assert response.status_code == 508
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "Invalid msisdn"

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)


def test_consent_req_invalid_entityid_09():
    #---------------------------------------------------------------------------------------------------------------------------------------
    #-----Verify that system returns error status with message for providing invalid entityid-----------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0].update({"entityid": "110163553000000226245"})
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
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

def test_consent_req_invalid_constempid_10():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----------Verify that system returns error status with message for providing invalid constempid-----------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0].update({"constempid": "110816443885823281345"})
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("#######", response.text)
    # Validate Response code
    breakpoint()
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_consent_req_invalid_source_11():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----------Verify that system returns error status with message for providing invalid source-----------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    input_json_dict["consent_registration"][0].update({"source": "8"})
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("#######", response.text)
    # Validate Response code
    breakpoint()
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid argument value"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_consent_register_req_api_faces_internal_error_12():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for any valid consent registration request API faces internal error"----------
    #---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    # input_json_dict["consent_registration"][0]["msisdn"] = "78876949469"
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 500
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "System error"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_another_consent_register_req_within_1month_13():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message when user sends another consent registeration request within 1 month from consent acquisition date"----------
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
    assert response.status_code == 500
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "System error"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_another_consent_register_req_within_3month_14():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message when user sends another consent registeration request within 3 months from consent acquisition date"----------
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
    assert response.status_code == 407
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Request is not accepted for 3 months from Consent acquisition date"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_sends_consent_register_req_already_registered_15():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message when user sends consent registeration request for already registered consent and in revoked state."----------
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
    assert response.status_code == 408
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Consent is in revoked state. Kindly ask subscriber to manage consent status on operator app/page "
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_consent_already_registered_for_particular_data_16():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for consent acquisition request when consent already exists for a particular MSISDN, Entityid, Constempid and Source."----------
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
    assert response.status_code == 409
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] ==  "Consent already exists"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_providing_entityid_inactive_account_17():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for providing entityid of an inactive account"----------
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
    assert response.status_code == 503
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Peid not active"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_using_http_GET_PUT_consent_registration_api_18():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for using http methods like GET or PUT for consent registeration request API."----------
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
    assert response.status_code == 405
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Invalid method"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_duplicate_consent_registration_req_19():
    #----------------------------------------------------------------------------------------------------------------------------------------
    #-----"Verify that system returns error status with message for sending another duplicate consent registeration request-----------------
    #----when the last request is in initiated state and still in pending state as subscriber has not accepted or rejected the consent."----------
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
    assert response.status_code == 406
    response_data = json.loads(response.text)
    print("Json response ------",response_data)
    assert response_data["message"] == "Duplicate request - Initiated status"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_with_IP_not_whitelisted_20():
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # -----Verify that system returns error status with message when user try to register consents from system whose IP is not whitelisted----------
    # ---------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 506
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "IP not whitelisted"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)

def test_consent_registration_with_diff_entityid_21():
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # -----Verify that system returns error status with message when authorization token is generated for a ----------------------------------------------------------------------------------------
    # -------particular entityid but consent registeration request created for a different entityid---------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "consent_registration.json"))
    request_json = json.dumps(input_json_dict["consent_registration"][0])
    response = post_call(get_endpoint_consent_registration(), request_json, get_headers_valid_token())
    input_json_dict["consent_registration"][0]["entityid"] = "1101635530000002261"
    print("##url##", get_endpoint_consent_registration())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    print("#header#", get_headers_valid_token())
    # Validate Response code
    assert response.status_code == 507
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "Peid mismatch"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)