import configparser


def load_db_config(database_name):
    host = get_db_config(database_name, 'host')
    user = get_db_config(database_name, 'user')
    password = get_db_config(database_name, "password")
    database = get_db_config(database_name, "database")
    port = get_db_config(database_name, "port")
    # Access values from the configuration file

    # Return a dictionary with the retrieved values
    config_values = {
        'host': host,
        'user': user,
        'password': password,
        'database': database,
        'port': port
    }

    return config_values


def get_db_config(config_type, config_name):
    config_parser = configparser.ConfigParser()
    config_parser.read('./Config/database_config.ini')

    if config_parser.has_option(config_type, config_name):
        config_value = config_parser.get(config_type, config_name)
    else:
        config_value = None

    return config_value


''' if __name__ == "__main__":
    # Call the function to read the configuration file
    config_data = load_db_config('MySql')

    # Print the retrieved values
    print("Host: ", config_data['host'])
    print("User:", config_data['user'])
    print("Database Name:", config_data['db_name'])
    print("Database Host:", config_data['db_host'])
    print("Database Port:", config_data['db_port'])  '''
