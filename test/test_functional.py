import unittest
import numpy as np
from mainclass import SalesAnalysis
from test.TestUtils import TestUtils


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.product1_sales = [50, 30, 20, 40, 10]
        self.product2_sales = [30, 50, 40, 10, 60]
        self.sales_analysis = SalesAnalysis(self.product1_sales, self.product2_sales)

    def test_add_sales(self):
        """Test if element-wise addition of sales works correctly."""
        obj = self.sales_analysis.add_sales()
        expected = np.array([80, 80, 60, 50, 70], dtype=np.int32)
        test_obj = TestUtils()
        if np.array_equal(obj, expected):
            test_obj.yakshaAssert("TestAddSales", True, "functional")
            print("TestAddSales = Passed")
        else:
            test_obj.yakshaAssert("TestAddSales", False, "functional")
            print("TestAddSales = Failed")

    def test_subtract_sales(self):
        """Test if element-wise subtraction of sales works correctly."""
        obj = self.sales_analysis.subtract_sales()
        expected = np.array([20, -20, -20, 30, -50], dtype=np.int32)
        test_obj = TestUtils()
        if np.array_equal(obj, expected):
            test_obj.yakshaAssert("TestSubtractSales", True, "functional")
            print("TestSubtractSales = Passed")
        else:
            test_obj.yakshaAssert("TestSubtractSales", False, "functional")
            print("TestSubtractSales = Failed")

    def test_calculate_mean(self):
        """Test if mean of total sales is correctly calculated."""
        obj = self.sales_analysis.calculate_mean()
        expected = 68.0
        test_obj = TestUtils()
        if obj == expected:
            test_obj.yakshaAssert("TestCalculateMean", True, "functional")
            print("TestCalculateMean = Passed")
        else:
            test_obj.yakshaAssert("TestCalculateMean", False, "functional")
            print("TestCalculateMean = Failed")

    def test_calculate_median(self):
        """Test if median of total sales is correctly calculated."""
        obj = self.sales_analysis.calculate_median()
        expected = 70.0
        test_obj = TestUtils()
        if obj == expected:
            test_obj.yakshaAssert("TestCalculateMedian", True, "functional")
            print("TestCalculateMedian = Passed")
        else:
            test_obj.yakshaAssert("TestCalculateMedian", False, "functional")
            print("TestCalculateMedian = Failed")