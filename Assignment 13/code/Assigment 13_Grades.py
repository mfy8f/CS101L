import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33)
    
    def test_total_returns_0(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,0)

    def test_average_one(self):
        values = (2,5,9)
        self.assertAlmostEqual(Grades.average(values),5.33333,5)

    def test_average_two(self):
        values = (2,15,22,9)
        self.assertAlmostEqual(Grades.average(values),12.0000,4)
    
    def test_average_returns_nan(self):
        values = ()
        self.assertIs(Grades.average(values),math.nan)

    def test_0(self):
        self.assertRaises(ValueError)

    def test_median(self):
        if len(self) <=0 :
            raise ValueError

unittest.main()

