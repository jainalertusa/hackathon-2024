from Dao.MySqlDao import save_properties, get_all_properties
from Utilities.load_webdata_configs import load_webdata_config
from scripts.web_scrapping import get_web_data
import time


def fetch_trulia_data():
    trulia_configs = load_webdata_config('Trulia')

    time.sleep(25)  # To ensure db is initialized.
    response = get_web_data(trulia_configs['url'], trulia_configs['headers'], trulia_configs['cookies'],
                            trulia_configs['json_data'], trulia_configs['params'])

    json_result = response.json()

    properties = json_result['data']['searchResultMap']['homes']

    save_properties(properties)

    print("Trulia Data Saved")


def get_trulia_data():
    return get_all_properties()
