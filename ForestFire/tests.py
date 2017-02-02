import unittest
import fire
import numpy as np

class TestField(unittest.TestCase):
	
	def create_small_field(self):
		f = fire.Field()
		f.grass = np.zeros((10,10), np.double)
		return f
		
	def test_grass_growth(self):
		f = self.create_small_field()	
		f = f.grass_grow()
		self.assertFalse(np.any(f.grass - 0.01))
		
	def test_for_each(self):
		field = self.create_small_field()
		
		actual = np.zeros_like(field.grass, dtype = np.bool)
		
		def func(x,y,value):
			actual[x,y]=True
			
		field.for_each(func)
		
		self.assertTrue(np.all(actual))

if __name__ == '__main__':
	unittest.main(verbosity=2)
