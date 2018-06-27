import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]
    def testMap(self):
        self.assertEqual([1,4,9,16,25],self._.map(self.test_list[:], lambda x:x**2))
    def testReduce(self):
        pass
    def testFind(self):
        pass
    def testFilter(self):
        pass
    def testReject(self):
        pass
if __name__ == "__main__":
    unittest.main()