"""
Author: Kitutu Paul
March, 2019
"""
import unittest
from ferry import Ferry
from vehicle import Vehicle


class TestFerryTerminal(unittest.TestCase):
	vehicle1 = Vehicle()
	ferry1 = Ferry()
	
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


if __name__ == '__main__':
	unittest.main()