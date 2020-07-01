import unittest
from locator import Locator
import pandas as pd


class TestDataParser(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_validate_top_k_elements_from_the_end(self):
        """
        This test validates if the 5 food trucks found at the sorted end in the csv file matches with the one found by invoking the locator API.
        """
        data = pd.read_csv("Mobile_Food_Facility_Permit.csv") 
        locator = Locator(37.807, -122.42)
        list_of_food_trucks = locator.get_food_trucks(5)
        sort1 = data.sort_values('Latitude', ascending=False)
        sort1 = sort1.head(5)
        for row in sort1.itertuples():
            match_found = False
            for list_of_food_truck in list_of_food_trucks:
                if list_of_food_truck.location_name == row.Applicant:
                    match_found=True
                    break
            self.assertTrue(match_found)
    
    def test_validate_top_k_elements_from_the_top(self):
        """
        This test fetches top elements from a sorted csv file based on Latitude.
        It compares the list of food trucks obtained from the locator API call with the values obtained from the top elements obtained from the csv file and asserts if it could not find a food truck in it.
        """
        data = pd.read_csv("Mobile_Food_Facility_Permit.csv") 
        locator = Locator(37.7093, -122.404)
        list_of_food_trucks = locator.get_food_trucks(5)
        sort1 = data.sort_values('Latitude', ascending=True)
        for row in sort1.itertuples():
            if row.Latitude == 0 or row.Longitude == 0:
                sort1 = sort1.drop(index=row.Index)
        sort1 = sort1.head(10)
        for list_of_food_truck in list_of_food_trucks:
            match_found = False
            for row in sort1.itertuples():
                if list_of_food_truck.location_name == row.Applicant:
                    match_found=True
                    break
            self.assertTrue(match_found)
    
    def tearDown(self):
        pass


if __name__ == "__main__":
    try:
        # To avoid the end of execution traceback adding exit=False
        unittest.main(exit=False)
    except:
        print("Exception occurred.{}".format(sys.exc_info()))
        print("Exception in user code:")
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)