import uniitest
# https://docs.python.org/3/library/unittest.html
"""Syntax testing a function
class NamesTestCase(uniitest.TestCase):   # inherit from TestCase
  
  def test_name_function(self):   # methods' name started with test_ will run automatically
    result = function(args)
    self.assertEqual(result, expected_rlt)

if __name__ == '__main__':
    unittest.main()

assertEqual(a, b)       Verify that a == b
assertNotEqual(a, b)    Verify that a != b
assertTrue(x)           Verify that x is True
assertFalse(x)          Verify that x is False
assertIn(item, list)    Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
...
"""

"""testing a class
"""

"""
setUp() : method called to prepare the test fixture. Called before calling the test method
tearDwon() : method called immediately after the test method has been called and the result recorder
setUpClass()  : A class method called before tests in an individual class are run
tearDownClass() : A class method called after tests in an individual class have run. 
"""

def setUp(self):
  pass

def tearDown(self):
  pass

@classmethod
def setUpCalss(cls):
  pass

@classmethod
def tearDownClass(cls):
  pass

"""
If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

Such a working environment for the testing code is called a test fixture. 
A new TestCase instance is created as a unique test fixture used to execute each individual test method. 
Thus setUp(), tearDown(), and __init__() will be called once per test.
"""

