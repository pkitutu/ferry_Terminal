"""
Author: Kitutu Paul
March, 2019
"""

class Ferry(object):
	"""docstring for Ferry"""
	vehicle_types = ()
	__max_vehicles = 0
	current_vehicles = 0
	__ferry_size = ''

	def __init__(self):
		super(Ferry, self).__init__()

	def set_size(self, size):
		self.__ferry_size = size

	def get_size(self):
		return self.__ferry_size


	def set_vehicle_types(self, vehicle_types):
		self.vehicle_types = vehicle_types

	def set_max_vehicles(self, max_vehicles):
		self.__max_vehicles = max_vehicles

	def get_max_vehicles(self):
		return self.__max_vehicles

	def park_vehicle(self):
		if self.space_available():
			self.current_vehicles += 1
			print "Vehicle parked"
		else:
			print "Vehicle failed to park because of no space"

	def space_available(self):
		return self.current_vehicles<self.__max_vehicles

	def right_vehicle(self, vehicle_size):
		return self.__ferry_size==vehicle_size



# f = Ferry()
# f.park_vehicle()
# f.park_vehicle()
# f.park_vehicle()
# f.park_vehicle()
# print f.space_available()