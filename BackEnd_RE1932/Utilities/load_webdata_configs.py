import configparser
import json


def load_webdata_config(website_name):

    url = get_webdata_config(website_name, 'url')

    headers = get_webdata_config(website_name, 'headers')
    headers = json.loads(headers)

    cookies = get_webdata_config(website_name, 'cookies')
    cookies = json.loads(cookies)

    params = get_webdata_config(website_name, 'params')
    params = json.loads(params)

    json_data = get_webdata_config(website_name, 'json_data')
    json_data = json.loads(json_data)

    # Return a dictionary with the retrieved values
    config_values = {
        'url': url,
        'headers': headers,
        'cookies': cookies,
        'params': params,
        'json_data': json_data
    }

    return config_values

def get_webdata_config(config_type, config_name):
    config_parser = configparser.RawConfigParser()
    config_parser.read('./Config/webdata_config.ini')

    if config_parser.has_option(config_type, config_name):
        config_value = config_parser.get(config_type, config_name)
    else:
        config_value = None

    return config_value

if __name__ == "__main__":
    # Call the function to read the configuration file
    config_data = load_webdata_config("Trulia")

    # Print the retrieved values
    print("Url: ", config_data['url'])
    print("Headers: ", config_data['headers'])
