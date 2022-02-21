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


def test_callback_url_blank_MSISDN_16():
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
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "Invalid Argument value or type - msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))


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


def test_callback_url_blank_status_20():
    
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----"Verify that the system allows DLT platform to send the consent acquisition status is blank to call back URL mentioned in DLT portal."-------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"status": " "})
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


def test_callback_url_blank_expirydt_21():

    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----"Verify that the system allows DLT platform to send the consent acquisition expirydt is blank to call back URL mentioned in DLT portal."-------
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"expirydt": " "})
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


def test_callback_url_http_GET_PUT_22():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call back
    #-------------URL mentioned in DLT portal for using http methods like GET or PUT for callback url API request"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #########Using_GET_Method#################
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = get_call(get_endpoint_callback_url(), get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 405
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["detail"] == "Method \"GET\" not allowed."
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    #########Using_PUT_Method#################
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = put_call(get_endpoint_callback_url(),request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 405
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["detail"] == "Method \"PUT\" not allowed."
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

def test_callback_invalid_MSISDN_23():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call
    #-------------back URL mentioned in DLT portal for invalid MSISDN (size less than or more than 10 Chars)"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"msisdn": "74066511093456"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["detail"] == "Invalid Argument value or type - msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

def test_callback_invalid_MSISDN_start_with_91_24():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call back URL
    #-------------mentioned in DLT portal for invalid MSISDN ( starting with '91')"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"msisdn": "917406651109"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["detail"] ==  "Invalid Argument value or type - msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

def test_callback_invalid_MSISDN_not_starts_with_6_7_8_9_25():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call
    #--------------back URL mentioned in DLT portal for invalid MSISDN (not starting with '6/7/8/9')"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"msisdn": "5406651109"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 501
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["detail"] ==  "Invalid Argument value or type - msisdn"
    # assert response_data["error_response"]["error_message"]
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

def test_callback_invalid_cstid_26():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to call
    #--------------back URL mentioned in DLT portal for invalid cstid"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"cstid": "110163553000000226212"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_invalid_uts_27():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status-----
    #-------------to call back URL mentioned in DLT portal for invalid uts (uts size more than 20 chars)"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"uts": "10-01-2022 13:45:22345"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_invalid_uts_format_28():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to-------
    #------------call back URL mentioned in DLT portal for invalid uts (uts not in dd-mm-yyyy hh:mm:ss(24hrs format))"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"uts": "2022-10-01 13:45:22"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_invalid_source_29():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to-----------
    #----------call back URL mentioned in DLT portal for invalid source (source size more than 20 chars)"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0].update({"source": "SMSSMSSMSSMSSMSSMSSMS"})
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_invalid_expirydt_30():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to-----------
    #---------call back URL mentioned in DLT portal for invalid expirydt (expirydt size more than 20 chars)"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0]["expirydt"] = "10-01-2024 13:45:2224"
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)

def test_callback_invalid_expirydt_not_DMY_31():
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status to------------
    #-----------call back URL mentioned in DLT portal for invalid expirydt (expirydt not in dd-mm-yyyy hh:mm:ss(24hrs format))"-------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    input_json_dict["callback_url"][0]["expirydt"] = "2022-10-01 13:45:22"
    request_json = json.dumps(input_json_dict["callback_url"][0])
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("###response###", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 200
    response_data = json.loads(response.text)
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))
    # Assert Mandatory Field level validation errors
    validate_success_callback(response_data)


def test_callback_url_only_source_37():

    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status
    # ----------------to call back URL mentioned in DLT portal for providing only SOURCE parameter in payload"-------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    # clear the all payload data
    request_data = json.dumps(input_json_dict.clear())
    # add STATUS parameter in payload
    print("request_data", request_data)
    input_json_dict['source'] = "SMS"
    request_json = json.dumps(input_json_dict)
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

def test_callback_url_only_status_38():

    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status
    # ----------------to call back URL mentioned in DLT portal for providing only STATUS parameter in payload"-------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    # clear the all payload data
    request_data = json.dumps(input_json_dict.clear())
    print("request_data", request_data)
    # add STATUS parameter in payload
    input_json_dict['status'] = "ACCEPTED"
    request_json = json.dumps(input_json_dict)
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

def test_callback_url_only_expiredt_39():
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----"Verify that the system sends callback url request to retry queue when DLT platform sends the consent acquisition status
    # ----------------to call back URL mentioned in DLT portal for providing only expirydt parameter in payload"-------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    # clear the all payload data
    request_data = json.dumps(input_json_dict.clear())
    print("request_data", request_data)
    # add STATUS parameter in payload
    input_json_dict['expirydt'] = "10-01-2024 13:45:24"
    request_json = json.dumps(input_json_dict)
    response = post_call(get_endpoint_callback_url(), request_json, get_headers_valid_token())
    print("##url##", get_endpoint_callback_url())
    print("#request#", request_json)
    print("#######", response.text)
    print(response.status_code)
    # Validate Response code
    assert response.status_code == 502
    response_data = json.loads(response.text)
    print("Json response ------", response_data)
    assert response_data["message"] == "msisdn is required"
    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

def test_callback_url_ACCEPTED_no_expiredt_40():
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    # ----Verify that the system sends callback url request to retry queue when DLT platform sends the consent------------------------------------------
    # ---------acquisition status "ACCEPTED"  to call back URL mentioned in DLT portal for not providing------------------------------------------------
    # ----------------------------------expirydt parameter in payload-----------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------

    input_json_dict = json.loads(get_json_from_file("ConsentAPI", "callback_url.json"))
    # clear the all payload data
    request_data = json.dumps(input_json_dict.clear())
    print("request_data", request_data)
    input_json_dict["callback_url"][0].update({"status": "ACCEPTED"})
    request_json = json.dumps(input_json_dict)
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