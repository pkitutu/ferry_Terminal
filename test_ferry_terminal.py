"""
Author: Kitutu Paul
March, 2019
"""
import unittest
from ferry import Ferry
from vehicle import Vehicle
from car import Car
from van import Van
from bus import Bus
from truck import Truck

class TestFerryTerminal(unittest.TestCase):
	vehicle1 = Vehicle()
	ferry1 = Ferry()
	car1 = Car()
	van1 = Van()
	bus1 = Bus()
	truck1 = Truck()


	
	#test functions of vehicle size
	def test_vehicle_size(self):
		self.vehicle1.set_size('small')
		self.assertEqual(self.vehicle1.get_size(), 'small')

	#test functions about vehicle gas
	def test_vehicle_gas(self):
		self.vehicle1.set_current_gas(10)
		self.assertEqual(self.vehicle1.get_current_gas(), 10)
		self.vehicle1.add_gas(20)
		self.assertEqual(self.vehicle1.get_current_gas(), 30)

	#test price functions of the vehicle
	def test_vehicle_price(self):
		self.vehicle1.set_price(3)
		self.assertEqual(self.vehicle1.get_price(), 3)

	def test_max_vehicles_on_ferry(self):
		self.ferry1.set_max_vehicles(6)
		self.assertEqual(self.ferry1.get_max_vehicles(), 6)

	def test_vehicle_parking_on_ferry(self):
		self.ferry1.set_max_vehicles(2)
		self.assertEqual(self.ferry1.get_max_vehicles(), 2)
		self.assertTrue(self.ferry1.space_available())
		self.ferry1.park_vehicle()
		self.assertTrue(self.ferry1.space_available())
		self.ferry1.park_vehicle()
		self.assertFalse(self.ferry1.space_available())

	def test_car_price(self):
		self.assertEqual(self.car1.get_price(), 3)

	def test_van_price(self):
		self.assertEqual(self.van1.get_price(), 4)

	def test_bus_price(self):
		self.assertEqual(self.bus1.get_price(), 5)

	def test_truck_price(self):
		self.assertEqual(self.truck1.get_price(), 6)


if __name__ == '__main__':
	unittest.main()