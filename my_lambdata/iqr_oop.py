# my_lambdata\iqr_oop.py

# IQR function written in terms of OOP
# Must feed in list of numbers

import numpy
import pandas

class Numbers():
    def __init__(self):
        pass
    
    def iqr(self, X):
        q1 = numpy.percentile(X, 25, interpolation='midpoint')
        q3 = numpy.percentile(X, 75, interpolation='midpoint')        
        print(f'The IQR for this data set is {q3 - q1}')

if __name__ == "__main__":

    data = pandas.DataFrame([1,2,3,4,5])
    nums = Numbers()

    nums.iqr(data)