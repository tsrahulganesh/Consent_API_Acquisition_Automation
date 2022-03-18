import json
import os

import pandas
import pyodbc
import requests
# from mysql.connector import connect

from TestCase.accessToken import access_key, access_key_expired

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NjkzNDI2LCJqdGkiOiIxYzYyNzUyZTdlMGI0MzFjOWUxNTA2ZjNjOTgyNzM1ZSIsInVzZXJfaWQiOjM4LCJlbnRpdHlpZCI6IjE0MDE1ODA0OTAwMDAwMDAwMjMifQ.BrQPzpjoKvfm4S3GYgikEAB5Zho8UATVcGbHymyLDC8"

global report_download_input


def get_headers_valid_token():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    return custom_headers
    print(custom_headers)


def get_headers_valid_token_expired():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_key_expired()
    }
    return custom_headers
    print(custom_headers)


def get_headers_valid_access_key():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_key()
    }

    return custom_headers


def get_headers_valid_access_key_xml_content_type():
    custom_headers = {
        "Content-Type": "application/xml",
        "Authorization": "Bearer " + access_key()
    }

    return custom_headers


def get_headers_valid_access_key_expired():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_key_expired()
    }

    return custom_headers


def get_headers_invalid_token():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token + "12"
    }

    return custom_headers


def get_headers_invalid_JWTToken():
    custom_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFtc1Fac2dRTEphMjRlb"
    }

    return custom_headers


def get_headers_without_Authorization():
    custom_headers = {
        "Content-Type": "application/json"
    }

    return custom_headers


def get_xml_headers_valid_token():
    custom_headers = {
        "Content-Type": "application/xml",
        "Authorization": "Bearer " + access_token
    }

    return custom_headers


def get_json_from_file(parent_dir, file_name):
    print("Read from Input JSON file")
    cur_path = os.path.dirname(__file__)
    print("\n" + cur_path)
    print("\n" + parent_dir)
    print("\n" + file_name)

    input_file_path = os.path.join(cur_path, '..', 'DataBags', parent_dir, file_name)
    print("\n" + input_file_path)

    input_file = open(input_file_path, 'r', encoding="utf8")
    json_input = input_file.read()
    # input_json = json.loads(json_input)

    return json_input


def get_empty_request():
    return "{}"


def validate_field_mandatory_error(response_dict, attribute_name):
    assert response_dict[attribute_name] != "This field is required."


def validate_NoAuthHeader(response_dict):
    assert response_dict["messages"] == "Invalid auth header. No credentials provided."


def validate_invalid_JWT_token(response_dict):
    assert response_dict["messages"] == "Invalid JWT token"


def validate_expired_token(response_dict):
    assert response_dict["messages"] == "Expired signature"
    #assert response_dict["data"] == "Opps! Internal server error"

def validate_success_callback(response_dict):
    assert response_dict["message"] == "Success"



def post_call(url, request_json, custom_headers):
    # Make Post call with json input param
    try:
        response = requests.post(url, request_json, headers=custom_headers, timeout=10)
        return response
    except requests.Timeout:
        print("Response is going to exceed the timeout of 10 sec")

    except requests.ConnectionError:
        print("ENT-endpoint is Down:")
        return -1


def put_call(url, request_json, custom_headers):
    # Make Put call with json input param
    try:
        response = requests.put(url, request_json, headers=custom_headers, timeout=5)
        return response

    except requests.Timeout:
        print("Response is going to exceed the timeout of 5 sec")

    except requests.ConnectionError:
        print("ENT-endpoint is Down:")
        return -1


def get_call(url, custom_headers):
    # Make Get call with json input param
    try:
        response = requests.get(url, headers=custom_headers, timeout=25)
        return response
    except requests.Timeout:
        print("Response is going to exceed the timeout of 5 sec")

    except requests.ConnectionError:
        print("ENT-endpoint is Down:")
        return -1


def delete_call(url, custom_headers):
    # Make Delete call with json input param
    try:
        response = requests.delete(url, headers=custom_headers, timeout=5)
        return response
    except requests.Timeout:
        print("Response is going to exceed the timeout of 5 sec")

    except requests.ConnectionError:
        print("ENT-endpoint is Down:")
        return -1


def fetch_data_from_db(query):
    host = "20.193.227.156"
    port = 31010
    uid = "admin-dremio"
    pwd = "dremio_tanla@1234"
    driver = "Dremio Connector"
    connection = pyodbc.connect(
        "Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(driver, host,
                                                                                                        port, uid, pwd),
        autocommit=True)

    sql = query

    dataframe = pandas.read_sql(sql, connection)
    print(dataframe)
    return dataframe


def fetch_invalid_dlr_report_request_id():
    host = "20.193.227.156"
    port = 31010
    uid = "admin-dremio"
    pwd = "dremio_tanla@1234"
    driver = "Dremio Connector"
    connection = pyodbc.connect(
        "Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(driver, host,
                                                                                                        port, uid, pwd),
        autocommit=True)

    sql = '''SELECT * FROM TanlaConfigDB_Test.dlr.delivery_report_overview where report_type != 'dlr' limit 1'''

    dataframe = pandas.read_sql(sql, connection)
    print(dataframe)
    return dataframe


def validate_create_rule_response(request_dict, response_dict):
    assert response_dict["data"]["ftpRuleId"] >= 0
    assert response_dict["data"]["isAdvancedRule"] == request_dict["isAdvancedRule"]

    assert response_dict["data"]["subAccount"]["id"] == request_dict["subAccount"]["id"]

    assert response_dict["data"]["subAccount"]["name"] == request_dict["subAccount"]["name"]

    assert response_dict["data"]["subAccount"]["username"] == request_dict["subAccount"]["username"]

    assert response_dict["data"]["subAccountPassword"] == request_dict["subAccountPassword"]

    assert response_dict["data"]["subAccountPassword"] == request_dict["subAccountPassword"]

    assert response_dict["data"]["credentialFtpType"] == request_dict["credentialFtpType"]

    assert response_dict["data"]["host"] == request_dict["host"]

    assert response_dict["data"]["port"] == request_dict["port"]

    assert response_dict["data"]["username"] == request_dict["username"]

    assert response_dict["data"]["password"] == request_dict["password"]

    assert response_dict["data"]["sourceDirectory"] == request_dict["sourceDirectory"]

    assert response_dict["data"]["sourceType"] == request_dict["sourceType"]

    assert response_dict["data"]["destinationFolder"] == request_dict["destinationFolder"]

    assert response_dict["data"]["whenToProcessFile"] == request_dict["whenToProcessFile"]

    if "needCheckerApproval" not in request_dict:
        assert response_dict["data"]["needCheckerApproval"] == False
    else:
        assert response_dict["data"]["needCheckerApproval"] == request_dict["needCheckerApproval"]

    if response_dict["data"]["isAlert"]:
        assert response_dict["data"]["isAlert"] == request_dict["isAlert"]
        assert response_dict["data"]["alertMobileNumbers"].sort() == request_dict[
            "alertMobileNumbers"].sort(), "Alert Mobile Numbers are not saved"
        assert response_dict["data"]["alertEmailAddresses"].sort() == request_dict["alertEmailAddresses"].sort()
    else:
        assert response_dict["data"]["isAlert"] == request_dict["isAlert"]
        assert response_dict["data"]["alertMobileNumbers"] == []
        assert response_dict["data"]["alertEmailAddresses"] == []

    # "pollEndTime": "2021-10-22T23:59"

    assert response_dict["data"]["pollFrequency"] == request_dict["pollFrequency"]

    assert response_dict["data"]["pollFilePattern"] == request_dict["pollFilePattern"]

    if not request_dict["isAdvancedRule"]:
        # assert response_dict["data"]["pollStartTime"] == datetime.date.strftime("%Y-%m-%dT%H:%M:%SZ")
        # assert response_dict["data"]["pollEndTime"] == datetime.date.strftime("%Y-%m-%dT%H:%M:%SZ")

        assert response_dict["data"]["fileType"] == "TXT"
        assert response_dict["data"]["delimeter"] == "|"
        assert response_dict["data"]["qualifier"] == "\""
        assert response_dict["data"]["isFileSecured"] == False
        assert response_dict["data"]["isFileZipped"] == False
        assert response_dict["data"]["isFilePasswordProtected"] == False
        assert response_dict["data"]["isFileEncrypted"] == False

        assert response_dict["data"]["isHeaderAvailable"] == False
        assert response_dict["data"]["isAdditionalAttribute"] == False
        assert response_dict["data"]["defineMessageForFile"] == False
        assert response_dict["data"]["isMultiTemplate"] == False
        assert response_dict["data"]["templateColumnName"] is None

        assert response_dict["data"]["secureReport"] == False
        assert response_dict["data"]["zipReport"] == False
        assert response_dict["data"]["passwordProtectReport"] == False

        assert response_dict["data"]["reportDirectory"] is None
        assert response_dict["data"]["reportProtectectionPassword"] is None
        assert response_dict["data"]["reportEncryptionParaphrase"] is None
        assert response_dict["data"]["reportOpenPgpEncryptionKey"] is None
    else:
        assert request_dict["pollStartTime"] in response_dict["data"]["pollStartTime"]
        assert request_dict["pollEndTime"] in response_dict["data"]["pollEndTime"]

        assert response_dict["data"]["fileType"] == request_dict["fileType"]
        assert response_dict["data"]["delimeter"] == request_dict["delimeter"]
        assert response_dict["data"]["qualifier"] == request_dict["qualifier"]
        assert response_dict["data"]["isFileSecured"] == request_dict["isFileSecured"]
        assert response_dict["data"]["isFileZipped"] == request_dict["isFileZipped"]

        if response_dict["data"]["isFilePasswordProtected"]:
            assert response_dict["data"]["isFilePasswordProtected"] == request_dict["isFilePasswordProtected"]
            assert response_dict["data"]["fileProtectionPassword"] == request_dict["fileProtectionPassword"]
        else:
            assert response_dict["data"]["isFilePasswordProtected"] == False
            assert response_dict["data"]["fileProtectionPassword"] is None

        assert response_dict["data"]["isFileEncrypted"] == request_dict["isFileEncrypted"]

        assert response_dict["data"]["isHeaderAvailable"] == request_dict["isHeaderAvailable"]
        assert response_dict["data"]["isAdditionalAttribute"] == request_dict["isAdditionalAttribute"]
        assert response_dict["data"]["defineMessageForFile"] == request_dict["defineMessageForFile"]
        assert response_dict["data"]["isMultiTemplate"] == request_dict["isMultiTemplate"]
        assert response_dict["data"]["templateColumnName"] == request_dict["templateColumnName"]

        if request_dict["clickReport"]:
            assert response_dict["data"]["clickReport"] == request_dict["clickReport"]
            assert response_dict["data"]["reportDirectory"] == request_dict["reportDirectory"]
            assert response_dict["data"]["clickReportParameters"] == request_dict["clickReportParameters"]

        else:
            assert response_dict["data"]["clickReport"] == False
            assert response_dict["data"]["reportDirectory"] is None

        if request_dict["deliveryReport"]:
            assert response_dict["data"]["deliveryReport"] == request_dict["deliveryReport"]
            assert response_dict["data"]["reportDirectory"] == request_dict["reportDirectory"]
            assert response_dict["data"]["clickReportParameters"] == request_dict["clickReportParameters"]

        else:
            assert response_dict["data"]["deliveryReport"] == False
            assert response_dict["data"]["reportDirectory"] is None

        assert response_dict["data"]["secureReport"] == request_dict["secureReport"]
        assert response_dict["data"]["zipReport"] == request_dict["zipReport"]

        if request_dict["passwordProtectReport"]:
            assert response_dict["data"]["passwordProtectReport"] == request_dict["passwordProtectReport"]
            assert response_dict["data"]["reportProtectectionPassword"] == request_dict["reportProtectectionPassword"]
            assert response_dict["data"]["reportEncryptionParaphrase"] == request_dict["reportEncryptionParaphrase"]
            assert response_dict["data"]["reportOpenPgpEncryptionKey"] == request_dict["reportOpenPgpEncryptionKey"]

        else:
            assert response_dict["data"]["passwordProtectReport"] == False
            assert response_dict["data"]["reportProtectectionPassword"] is None
            assert response_dict["data"]["reportEncryptionParaphrase"] is None
            assert response_dict["data"]["reportOpenPgpEncryptionKey"] is None
