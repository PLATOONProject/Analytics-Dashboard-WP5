# Some best practices:
#     * Tests should be independent from each other (they don´t execute in order)
#     * The name of the test should be informative v.g. test_[name_of_function]
#     * Document each test

import unittest
# from [script_name] import [objects_to_be_tested]


# replace ObjectName for the name of the object to be tested!!
class TestObjectName(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # It will run once before tests start
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        # It will run once after all test have finished
        print('teardownClass')

    def setUp(self):
        # setUp function will run before every test
        print('setUp')

    def tearDown(self):
        # tearDown function will run after every test
        print('tearDown')

    # replace testname for something more informative!!
    def test_testname1(self):
        # Run the test number 1
        print('Running Test 1')

    def test_testname2(self):
        # Run the test number 1
        print('Running Test 2')


if __name__ == '__main__':
    unittest.main()
