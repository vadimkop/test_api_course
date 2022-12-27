import datetime
import os
from requests import Response


class Logger:
    file_name = f"C:/Users/vadko/Test/api_pytest/logs/log_" + \
                str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_add = f"\n-----\n"
        data_add += f"Test: {test_name}\n"
        data_add += f"Time: {str(datetime.datetime.now())}\n"
        data_add += f"Request method: {method}\n"
        data_add += f"Request url: {url}\n"
        data_add += "\n"

        cls.write_log_file(data_add)

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_add = f"Response code: {result.status_code}\n"
        data_add += f"Response text: {result.text}\n"
        data_add += f"Response headers: {headers_as_dict}\n"
        data_add += f"Response cookies: {cookies_as_dict}\n"
        data_add += f"\n-----\n"

        cls.write_log_file(data_add)