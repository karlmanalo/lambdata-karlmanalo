# my_lambdata\iqr_oop.py

# IQR function written in terms of OOP

class IQR():
    def __init__(self):
        
    
    def iqr(self):
        q1 = numpy.percentile(self, 25, interpolation='midpoint')
        q3 = numpy.percentile(self, 75, interpolation='midpoint')        
        print(f'The IQR for this data set is {q3 - q1}')

if __name__ == "__main__":

    data = IQR([1,2,3,4,5])
    print(IQR.iqr)