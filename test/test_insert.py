import  unittest
from insert_value import insert_val_at

class InsertValueTest(unittest.TestCase):
	def setUp(self):
		self.test_list = [0,1,2,3,4]
		self.result = insert_val_at(2, self.test_list[:],100)

		self.result2 = insert_val_at(7, self.test_list[:],100)

	def test_insert_at_index_two(self):
		return self.assertEqual([0,1,100,2,3,4], self.result)

	def test_return_false_for_invalid_index(self):
		return self.assertFalse(self.result2)

if __name__ == '__main__':
	unittest.main()