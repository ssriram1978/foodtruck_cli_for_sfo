"""
This file contains the code for argparser for food truck locator.
"""
from locator import Locator
import argparse

def latitude_validator(string):
    """
    The latitude has the symbol of phi, and it shows the angle between the straight line in the certain point and the equatorial plane. The latitude is specified by degrees, starting from 0° and ending up with 90° to both sides of the equator, making latitude Northern and Southern. 
    :input string
    :return float
    """
    value = float(string)
    if value < -90 or value > 90:
        raise argparse.ArgumentTypeError("Latitude {} is invalid.".format(value))
    return value

def longitude_validator(string):
    """
    The longitude has the symbol of lambda and is another angular coordinate defining the position of a point on a surface of earth. The longitude is defined as an angle pointing west or east from the Greenwich Meridian, which is taken as the Prime Meridian. The longitude can be defined maximum as 180° east from the Prime Meridian and 180° west from the Prime Meridian.
    :input string
    :return float
    """
    value = float(string)
    if value < -180 or value > 180:
        raise argparse.ArgumentTypeError("Longitude {} is invalid.".format(value))
    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-la", "--latitude", help="Latitude",
                    required=True, type=latitude_validator)
    parser.add_argument("-lo", "--longitude", help="Longitude",
                    required=True, type=longitude_validator)
    parser.add_argument("-m", "--max_num", help="Total number of closest points", required=False, type=int,default=5)
    args = parser.parse_args()
    # Instantiate an object of type Locator and pass in the current location latitude and longitude coordinates.
    locator = Locator(args.latitude, args.longitude)
    # Invoke the API get_food_trucks() exposed by the Locator instance and pass in the total number of locations to be fetched.
    list_of_food_trucks = locator.get_food_trucks(args.max_num)
    print("The list of food trucks closer to the current location Latitude: {}, Longitude: {} are:\n".format(args.latitude, args.longitude))
    for index, food_truck in enumerate(list_of_food_trucks):
        # Print the desired output
        print("{}. {}\n".format(index+1, food_truck))


