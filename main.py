from Lab5_Classes import Numbers, ECG
from unit_test import *
import math
import unittest

factorial_unit_testing_list = [5, 1, 0]

for i in range(len(factorial_unit_testing_list)):
    actual_result = math.factorial(factorial_unit_testing_list[i])
    expected_result = factorial_unit_testing(factorial_unit_testing_list[i])
    assert actual_result == expected_result, "Unit test has returned false, the actual result does not match the expected result"
    print("Unit test has returned true, the actual result matches the expected result\n")
    print("The actual value was", actual_result, "which matches the expected value of", expected_result)
    
class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.numbers = Numbers()  
    
    def test_factorial(self):
        self.assertEqual(self.numbers.factorial(5), 120)
        self.assertEqual(self.numbers.factorial(0), 1)
        self.assertRaises(ValueError, self.numbers.factorial, -1)

    def test_addToSum(self):
        self.numbers.addToSum(10)
        self.assertEqual(self.numbers.sum, 10)
        self.numbers.addToSum(5)
        self.assertEqual(self.numbers.sum, 15)

    def test_subtractFromSum(self):
        self.numbers.subtractFromSum(5)
        self.assertEqual(self.numbers.sum, 10)
        self.numbers.subtractFromSum(3)
        self.assertEqual(self.numbers.sum, 7)

    def test_stringOfNumber(self):
        self.assertEqual(self.numbers.stringOfNumber(3), "three")
        self.assertRaises(TypeError, self.numbers.stringOfNumber, "3")
        self.assertRaises(ValueError, self.numbers.stringOfNumber, 10)


class TestECG(unittest.TestCase):
    def setUp(self):
        self.ecg = ECG() 
        self.signal = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]
        self.threshold = 0.7
    
    def test_peaks_function(self):
        peaks = self.ecg.detect_peaks(self.signal)
        self.assertEqual(peaks, [2, 5])  

    def test_baseline_function(self):
        baseline_removed_signal = self.ecg.remove_baseline(self.signal)
        self.assertTrue(all(val >= 0 for val in baseline_removed_signal))

    def test_normalization_function(self):
        normalized_signal = self.ecg.normalize(self.signal)
        self.assertTrue(all(0 <= val <= 1 for val in normalized_signal))

    def test_is_signal_valid(self):
        self.assertTrue(self.ecg.is_signal_valid(self.signal))
        self.assertFalse(self.ecg.is_signal_valid([]))  
        self.assertFalse(self.ecg.is_signal_valid([None, 1.2, 3.4]))  

    def test_count_peaks(self):
        peak_count = self.ecg.count_peaks(self.signal, self.threshold)
        self.assertEqual(peak_count, 2)  

    def test_rr_intervals(self):
        peaks = self.ecg.detect_peaks(self.signal, self.threshold)
        rr_intervals = self.ecg.rr_intervals(peaks, 1)  
        self.assertEqual(rr_intervals, [3.0])  

    def test_heart_rate(self):
        peaks = self.ecg.detect_peaks(self.signal, self.threshold)
        heart_rate = self.ecg.heart_rate(peaks, 1)  
        self.assertEqual(heart_rate, 20)  
        
if __name__ == '__main__':
    unittest.main()