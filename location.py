from math import degrees, radians, sin, cos, acos, atan2, sqrt


class Location:
  """
  This class implements the functionality to compute the distance of all
  the food trucks from the user location.
  """
  def __init__(self, 
               location_latitude, 
               location_longitude,
               location_name,
               location_address,
               location_description,
               location_food,
               location_schedule,
               location_hours, 
               center_latitude, 
               center_longitude):
    self.location_latitude = radians(location_latitude)
    self.location_longitude = radians(location_longitude)
    self.center_latitude = radians(center_latitude)
    self.center_longitude = radians(center_longitude)
    self.location_name = location_name
    self.location_address = location_address
    self.location_description = location_description
    self.location_food = location_food
    self.location_schedule = location_schedule
    self.location_hours = location_hours
    # change in coordinates
    self.dlon = self.center_longitude - self.location_longitude
    self. dlat = self.center_latitude - self.location_latitude

  def __str__(self):
      """
      Return a string formatted output.
      :return string
      """
      return "Latitude = {}, Longitude = {}, Name = {}, Address = {}, Description = {}, Food = {}, Schedule = {}, Hours = {}.".format(degrees(self.location_latitude), degrees(self.location_longitude), self.location_name, self.location_address, self.location_description, self.location_food, self.location_schedule, self.location_hours)
      
  # used for max-heap
  def __lt__(self, other):
    """
      This method is used in maxheap to return True if the current distance from the origin is greater than the other Location else return False.
      Note that this is a less than method signature but it returns True if it is actually greater.
    :return True or False
    """
    return self.distance_from_origin() > other.distance_from_origin()

  def distance_from_origin(self):
    """
    This method computes the distance of the coordinate from the location of the user coordinates.
    :return distance
    """
    # https://kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
    #radius of the Earth
    R = 6373.0
    #Haversine formula    
    a = sin(self.dlat / 2)**2 + cos(self.location_latitude) * cos(self.center_latitude) * sin(self.dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #Compute the distance
    distance = R * c
    return distance