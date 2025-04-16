import unittest
import numpy as np
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils


class ExceptionalTests(unittest.TestCase):
    def test_empty_data_addition(self):
        """Test if empty sales data raises an error for addition."""
        test_obj = TestUtils()
        try:
            empty_data = SalesAnalysis([], [])
            empty_data.add_sales()
            test_obj.yakshaAssert("TestEmptyDataAddition", False, "exceptional")
            print("TestEmptyDataAddition = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyDataAddition", True, "exceptional")
            print("TestEmptyDataAddition = Passed")

    def test_empty_data_subtraction(self):
        """Test if empty sales data raises an error for subtraction."""
        test_obj = TestUtils()
        try:
            empty_data = SalesAnalysis([], [])
            empty_data.subtract_sales()
            test_obj.yakshaAssert("TestEmptyDataSubtraction", False, "exceptional")
            print("TestEmptyDataSubtraction = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyDataSubtraction", True, "exceptional")
            print("TestEmptyDataSubtraction = Passed")
