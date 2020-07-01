"""
This file implements the locator algorithm for food truck.
"""

from heapq import *
from os import path
import pandas as pd
from location import Location


class Locator:
    """
    This class helps in locating the food trucks in SFO for the pased in 
    latitude and longitude.
    
    """
    def __init__(self, center_latitude, center_longitude):
        data = pd.read_csv("Mobile_Food_Facility_Permit.csv") 
        # Intialize a points list to store all instances of Location class.
        self.points = []
        for row in data.itertuples():
            if row.Latitude == 0 or row.Longitude == 0:
                # Skip invalid rows.
                continue
            #Instantiate an object of type Location.
            location = Location(
               row.Latitude, 
               row.Longitude,
               row.Applicant,
               row.Address,
               row.LocationDescription,
               row.FoodItems,
               row.Schedule,
               row.dayshours, 
               center_latitude, 
               center_longitude)
            #Store it in points list.
            self.points.append(location)
            
    def get_food_trucks(self, total_num_of_closest_points):
        """
        This method returns a list of closest points near the user defined location.
        Note: minheap and maxheap from heapq is used because:
        1. It takes log N time complexity to move a Location to the correct sorted index where N is the total number of elements.
        2. The space complexity is N.
        3. maxHeap is used because we always want to compare the Xth min element from the heap which is on the top to swap out the top element from the heap with the remaining locations from the list in order of log N time complexity.
        4. Note that Heap is the best data structure that could be used for handling these kinds of situations where we need to find X number of location closer to the specified user current location coordinates.
        
        :return: list containing instances of type Location.
        """
        maxHeap = []
        # Push first 'total_num_of_closest_points' points in the max heap
        for i in range(total_num_of_closest_points):
            heappush(maxHeap, self.points[i])

        # For the remaining elements, check if the top element in the maxHeap is greater than the current element.
        # If so, then pop the top element out and push the current element back into the max heap.
        # The reason why we do this is because we want to keep only total_num_of_closest_points elements in the list. We do not want a location that is greater than the size of the list.
        for i in range(total_num_of_closest_points, len(self.points)):
            if self.points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
                heappop(maxHeap)
                heappush(maxHeap, self.points[i])

        # the heap has 'total_num_of_closest_points' points closest to the passed in coordinates, return them in a list.
        return list(maxHeap)