import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Unexpected status code - {response.status_code}"

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert expected_value == list(token), f"All or part of the required fields are missing: {list(token)}"

    @staticmethod
    def check_json_values(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert expected_value == check_info, f"Unexpected value for '{field_name}' field - {check_info}"

    @staticmethod
    def check_json_part_values(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert expected_value in check_info, f"Unexpected value for '{field_name}' field - {check_info}"
