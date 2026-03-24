import math

#Use ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2] for unit testing

import math

class Numbers:
    def __init__(self, sum=0):
        self.sum = sum

    #4.1
    def factorial(self, number) -> int:
        if number < 0:
            raise ValueError("Negative not allowed")
        return math.factorial(number)
    
    #4.2
    def addToSum(self, number) -> None:
        '''Add to the sum'''
        self.sum += number

    #4.3
    def subtractFromSum(self, number) -> None:
        '''Remove from the sum'''
        self.sum -= number

    #4.4
    def stringOfNumber(self, number) -> str:
        numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        if not isinstance(number, int):
            raise TypeError("Must be int")
        if 0 <= number <= 9:
            return numbers[number]
        raise ValueError("Out of range")


class ECG:
    def __init__(self):
        pass
    
    #5.1
    def detect_peaks(self, signal, threshold):
        '''
        Return list of peaks in an ECG signal
        
        A peak is such that it is a point above the threshold value,
        and is greater than the values to its left and right
        '''
        if len(signal) < 3:
            return []
        peaks = []
        for i in range(1, len(signal)-1):
            if signal[i] > threshold and signal[i] > signal[i-1] and signal[i] > signal[i+1]:
                peaks.append(i)
        return peaks

    #5.2
    def remove_baseline(self, signal):
        '''Remove the baseline from a provided signal'''
        if len(signal) == 0:
            raise ValueError("Signal cannot be empty")
        mean_val = sum(signal) / len(signal)
        return [x - mean_val for x in signal]
    
    #5.3
    def normalize(self, signal):
        '''Normalize a provided signal'''
        if len(signal) == 0:
            raise ValueError("Signal cannot be empty")
        max_val = max(abs(x) for x in signal)
        if max_val == 0:
            return signal
        return [x / max_val for x in signal]

    #6.1
    def count_peaks(self, signal, threshold):
        '''
        This function return the total number of peaks
        '''
        peaks = 0

        #Your Code Here

        return peaks

    #6.2
    def rr_intervals(self, peaks, fs):
        '''
        Calculate the time between consecutive peaks (RR intervals)

        peaks is a list of detected peak positions
        fs is the sampling frequency

        Returns a list of RR intervals in seconds
        '''
        intervals = []

        #Your Code Here

        return intervals
    
    #6.3
    def is_signal_valid(self, signal):
        '''
        Signal must
        - be a list
        - not empty
        - contain only numeric values

        Returns a boolean, True (1) if a proper signal, False (0) otherwise
        '''

    #7
    def heart_rate(self, peaks, fs):
        '''
        peaks is a list of detected peak positions
        fs is the sampling frequency
        
        This function should return the heart rate in (BPM)
        '''
        heartRate = 0

        #Your Code Here

        return heartRate