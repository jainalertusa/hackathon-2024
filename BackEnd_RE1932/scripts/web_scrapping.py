import requests


def get_web_data(url, headers, cookies, json_data, params):
    response = requests.post(url, headers=headers, cookies=cookies, json=json_data, params=params)
    return response
