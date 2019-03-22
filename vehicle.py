class Vehicle(object):
	"""docstring for Vehicle"""
	__size = ''
	__price = 0
	__current_gas = 0
	def __init__(self):
		super(Vehicle, self).__init__()

	def set_size(self, size):
		self.__size = size

	def get_size(self):
		return self.__size

	def set_price(self, price):
		self.__price = price

	def get_price(self):
		return self.__price

	def set_current_gas(self, gas):
		self.__current_gas = gas

	def get_current_gas(self):
		return self.__current_gas

	def add_gas(self, gas):
		self.__current_gas += gas