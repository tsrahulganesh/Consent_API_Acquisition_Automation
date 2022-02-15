import requests
import json
import jsonpath
import os
import time

def get_request_json():
    cur_path = os.path.dirname(__file__)
    input_file_path = os.path.join(cur_path, '..', 'DataBags', 'ConsentAPI', 'CreateRule.json')
    input_file = open(input_file_path, 'r', encoding="utf8")
    json_input = input_file.read()
    request_json = json.loads(json_input)

    return request_json


def access_key():
    # API URL
    url = "https://nldpreprodapim.tanla.com/login"

    custom_hdrs_login = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_type": "access_key"
    }
    # Read Input_json
    cur_path = os.path.dirname(__file__)
    print("Current Working Directory :" + cur_path)
    print(cur_path)
    new_path = os.path.join(cur_path, '..', 'DataBags', 'Config', 'login.json')

    print(new_path)
    input_file = open(new_path, 'r', encoding="utf8")

    # input_file = open("../DataBags/input_params_login.json", "r")
    json_input = input_file.read()
    request_json = json.loads(json_input)
    # Make Post call with json input param

    response = requests.post(url, request_json, headers=custom_hdrs_login, timeout=5)
    print("###########################")
    print(response.text)
    # Validate Response code
    # print(response.status_code)
    assert response.status_code == 200

    # Fetch Header from Response
    print(response.headers.get("Content-Type"))

    # Parse Response to json format
    response_json = json.loads(response.text)
    # Pick ID/Access-Token using json path
    access_token = jsonpath.jsonpath(response_json, "access_token")
    print(access_token[0])
    return access_token[0]

def access_key_expired():
    return "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCIsImtpZCI6Imwzc1EtNTBjQ0g0eEJWWkxIVEd3blNSNzY4MCJ9.eyJhdWQiOiJhcGk6Ly9ubGR0ZXN0LnRhbmxhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvODYxOThiM2YtYjQxMS00Y2NjLTlhZTMtODY3YjkxMzIyMjAwLyIsImlhdCI6MTYzNTE2MzMxOCwibmJmIjoxNjM1MTYzMzE4LCJleHAiOjE2MzUxNjcyMTgsImFjciI6IjEiLCJhaW8iOiJBU1FBMi84VEFBQUF0djF0d0xicUxYNE9kUVF5MEpmd2s2MXNhc0lYeHphdFl6TVlxUmFlSlNzPSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiI3MTNiMGNkMi0yNDc5LTQwYzAtYmU2OC04NzU3YzgwNGJiYTAiLCJhcHBpZGFjciI6IjAiLCJpcGFkZHIiOiIyMC4xOTcuNjAuMTMyIiwibmFtZSI6IkVOVDY5OTA0NyIsIm9pZCI6ImZhZWQ5ZGFhLWJhNWMtNDIwMi04MDgxLTU0NzNhMDQwYTA0MSIsInJoIjoiMC5BWEFBUDRzWmhoRzB6RXlhNDRaN2tUSWlBTklNTzNGNUpNQkF2bWlIVjhnRXU2QndBTkUuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiM3BOMW1Lc1RDZjVkMy04MUtoby16bF93ZkJGQkRKakhxY3A1VGJJTXBLRSIsInRpZCI6Ijg2MTk4YjNmLWI0MTEtNGNjYy05YWUzLTg2N2I5MTMyMjIwMCIsInVuaXF1ZV9uYW1lIjoiRU5UNjk5MDQ3QHRwbHdpc2VseXRlc3Qub25taWNyb3NvZnQuY29tIiwidXBuIjoiRU5UNjk5MDQ3QHRwbHdpc2VseXRlc3Qub25taWNyb3NvZnQuY29tIiwidXRpIjoiUVFNR1FQVmFxa2VxV0U0ay00UzZBQSIsInZlciI6IjEuMCJ9.bsYo-2HotvQr1vwS2OxiG61sOf3JgAec5vtXyz4B9yqdb9tn2TNoYbQwsXF5wZ6bCjPkf4NUfF9Qb3HM_2MdXIzr3NMZA0OUiqADoqW38jFs2aNa7vooogttpdBxpEn4VAIBG6bHL2-WakeBcIDDy1f_wuGAx-BEgvGK2D2PgK-yDsKrFQ88yoKCZUdF_6aZPOhCCOyK4JhOKhKc9z2Pwu75sS5bvQDJrxjrBIisqNavhExbKtZtogcv35Nuu3z-CByRaOKoDrHJ91lmK1gtz2ODF4BgAq3lidN9bcYCXMHqjqvaaLnOpjYf8YlCq6POA_fP5RmN-Exy41BF49iGQw"


def test_create_rule():
    url = "https://nldpreprodapim.tanla.com/portal/ftp/"
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Il9ab3ktWHB4M2UtallOYnhmaktXX1VlV3g2N3YzS2s1SDN1MlFYZ1oxM2sifQ.eyJpc3MiOiJodHRwczovL3dpc2VseXByZXByb2QuYjJjbG9naW4uY29tLzU2ZTY2NDAwLTQyNmUtNDdjMS05MTVhLWUwNmM3OTQzMmMxMC92Mi4wLyIsImV4cCI6MTY0MDAxMzg3OCwibmJmIjoxNjQwMDEwMjc4LCJhdWQiOiJhNWE4OGJiMC1jZGIyLTRiYzEtOTI2YS1hZTkwNGNlY2UzODEiLCJzdWIiOiJjMWFjODUyMi1mM2ZhLTQ0MDUtYTRjZC01ZjZkM2I0NWQ5MTciLCJleHRlbnNpb25fYXBwX3JvbGUiOiJTdXBlciBBZG1pbiIsImV4dGVuc2lvbl9kZWxlZ2F0ZWRfcm9sZSI6IiIsImV4dGVuc2lvbl9hY2NvdW50X2lkIjoiIiwiZXh0ZW5zaW9uX21vcmVfcGVybWlzc2lvbl9leGlzdHMiOmZhbHNlLCJleHRlbnNpb25fcGVybWlzc2lvbnMiOlsiLS5NYW5hZ2UgU01TIENvbm5lY3RzLi06RWRpdCxWaWV3LFZpZXciLCItLk1hbmFnZSBSb3V0aW5nLi06Q3JlYXRlL0FkZCxFZGl0LFZpZXciLCItLk1hbmFnZSBBUElzIEtleXMuLTpDcmVhdGUvQWRkLEVkaXQsVmlldyIsIi0uTWFuYWdlIFBhcnRuZXJzLi06Q3JlYXRlL0FkZCxFZGl0LFZpZXciLCItLk1hbmFnZSBMaW5RLi06Q3JlYXRlL0FkZCxFZGl0LFZpZXciLCItLk1hbmFnZSBGVFAuLTpDcmVhdGUvQWRkLEVkaXQsVmlldyIsIi0uTWFrZXIgXHUwMDI2IENoZWNrZXIuLTpDcmVhdGUvQWRkLEVkaXQsVmlldyIsIi0uUmVwb3J0cy5EYXNoYm9hcmQ6VmlldyxEb3dubG9hZCIsIi0uUmVwb3J0cy5DRFI6VmlldyxEb3dubG9hZCIsIi0uUmVwb3J0cy5TU09UOlZpZXcsRG93bmxvYWQiLCItLlJlcG9ydHMuU01TIC0gUk9JOlZpZXcsRG93bmxvYWQiLCItLlJlcG9ydHMuU01TIC0gUGVyZm9ybWFuY2U6VmlldyxEb3dubG9hZCIsIi0uUmVwb3J0cy5TZXR0bGVtZW50IFJlcG9ydDpWaWV3LERvd25sb2FkIiwiLS5SZXBvcnRzLkxpblEgQW5hbHl0aWNzOlZpZXcsRG93bmxvYWQiLCItLlJlcG9ydHMuRlRQIEFuYWx5dGljczpWaWV3LERvd25sb2FkIiwiLS5NYW5hZ2UgSWRlbnRpdHkgYW5kIEFjY2Vzcy4tOkNyZWF0ZS9BZGQsRWRpdCxWaWV3LERlbGV0ZSJdLCJ0aWQiOiI1NmU2NjQwMC00MjZlLTQ3YzEtOTE1YS1lMDZjNzk0MzJjMTAiLCJub25jZSI6IjExNjQxZTFmLWI3NjMtNGZlNi1hZGU2LTg4ZmYyNzdhMTgwNiIsInNjcCI6ImRlbW8ucmVhZCIsImF6cCI6IjNkYzk4YzQ4LTk1ZDEtNDhhMC05MDg4LThlNDcyNWJkMWNmMCIsInZlciI6IjEuMCIsImlhdCI6MTY0MDAxMDI3OH0.Dbxa9h37N7hYNUv59VC8rbUf_2YJEGLIfwoqzWsHpAlfQ8PxY9UssSlxfXmfYWe-D3aAEn2599MYeCb8kCP5LQktP6LxG6hOBOJPw-m5uytNkARUTIh-WICHvWvUKGQbBsSH9efZ4F7YG188IqmwOSkozTH5eYfyUGUJUoMsOf9GII43s8-71QQtIVgUzIfKXhjvpYbhV2A0pi9Xd4ZnAwTbScJUIPQakrJL2q6dn0hvycvBMpdOsGQqDctSZXklp7BjEv881cmOLctn-mEuXWRNLE_BHUebsJ8lXcw9844mqlaptBSP0qJyskAnfSLCPmjk5ZF6rdr4HVRoCRBULw"
    request_json = get_request_json()
    custom_hdrs = {
        "User-Agent": "PostmanRuntime/7.28.4",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + access_token
    }
    print("Headers \n")
    print(custom_hdrs)
    print("\nRequest Before Removing rule Name:\n")

    print(json.dumps(request_json))
    ##del request_json["subAccount"]["id"]
    request_json["subAccount"]["id"] = 100
    print("\nRequest After Removing rule Name:\n")

    print(json.dumps(request_json))
    response = ''
    # response = requests.get(url, headers=custom_hdrs)
    # print("##########",response.status_code)
    while response == '':
        try:
            response = requests.get(url, headers=custom_hdrs)
            print("##########",response.status_code)
            break
        except requests.exceptions.ConnectionError:
            # response.status_code = "Connection refused"
            print("Hitting Connection Error:::")
            time.sleep(5)
            continue

    print("###########################")

    # Validate Response code
    # print(response.status_code)
    assert response.status_code == 200
