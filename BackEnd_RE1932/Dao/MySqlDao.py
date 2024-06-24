import traceback

import mysql.connector

from Utilities.load_db_configs import load_db_config


def get_database_connection():
    db_configs = load_db_config("MySql")
    connection = mysql.connector.connect(host=db_configs['host'], user=db_configs['user'],
                                         password=db_configs['password'], port=db_configs['port'],
                                         database=db_configs['database'])

    #connection = mysql.connector.connect(host='localhost', user='root', password='Vishesh@21', database='BackEnd_RE1932')

    return connection


def save_properties(properties):
    insert_property_query = """INSERT INTO Properties(
           Price, Beds, Bath, Area)
           VALUES (%s, %s, %s, %s);"""

    insert_address_query = """INSERT INTO Address (
        HomeId, Zip, Street, City, State, Latitude, Longitude, Country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """

    connection = get_database_connection()

    try:
        with connection.cursor() as cursor:
            for property in properties:
                price = property['price']['calloutMarkerPrice'] if property['price'] is not None else 0

                beds = property['bedrooms']['formattedValue'] if property['bedrooms'] is not None else "0"

                bath = property['bathrooms']['formattedValue'] if property['bathrooms'] is not None else "0"

                area = property['floorSpace']['formattedDimension'] if property['floorSpace'] is not None else "0"

                area = area.replace(',', '')

                cursor.execute(insert_property_query, (price, beds, bath, area))

                home_id = cursor.lastrowid

                if property['location'] is not None:
                    latitude = property['location']['coordinates']['latitude'] if property['location'][
                                                                                      'coordinates'] is not None else 0
                    longitude = property['location']['coordinates']['longitude'] if property['location'][
                                                                                        'coordinates'] is not None else 0
                else:
                    latitude = 0
                    longitude = 0

                zipcode = property['location']['zipCode'] if property['location'] is not None else "0"

                street = property['location']['streetAddress'] if property['location'] is not None else "0"

                city = property['location']['city'] if property['location'] is not None else "0"

                state = property['location']['stateCode'] if property['location'] is not None else "0"

                cursor.execute(insert_address_query,
                               (home_id, zipcode, street, city, state, latitude, longitude, "USA"))

        connection.commit()
    except:
        connection.rollback()
        traceback.print_exc()
    finally:
        connection.close()


def get_all_properties():
    select_properties_query = """ SELECT p.HomeId,  p.Beds, p.Bath, p.Area, p.Price,
        a.Zip, a.Street, a.City, a.State, a.Latitude, a.Longitude, a.Country
        FROM Properties p JOIN Address a ON p.HomeId = a.HomeId"""

    connection = get_database_connection()

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(select_properties_query)
        properties = cursor.fetchall()
    except:
        properties = []
        traceback.print_exc()
    finally:
        connection.close()

    return properties
