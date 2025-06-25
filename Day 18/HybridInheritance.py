'''Task:
Create a parent class Number.
Create SumNumber and ProductNumber classes that inherit from Number.
Create a final class FinalCalculator that inherits from both.
Call parent methods directly:
SumNumber.sum(self, a, b).
ProductNumber.product(self, a, b).
Test:
FinalCalculator().sum(5, 10) → 15
FinalCalculator().product(3, 4) → 12'''
class Number:
    def __init__(self):
        pass
        # self.a  = a
        # self.b = b    

class SumNumber(Number):
    # def __init__(self, a, b):
    #     super().__init__()
    #     return a + b
    def sum(self, a, b):
        return a + b

class ProductNumber(Number):
    # def __init__(self, a, b):
    #     super().__init__(a, b)
    #     return a * b
    def product(self, a, b):
        return a * b

class FinalCalculator(SumNumber, ProductNumber):
    def sum(self, a, b):
        return super().sum(a, b)
    def product(self, a, b):
        return super().product(a, b)
       
    
print("Sum :", FinalCalculator().sum(5, 10))
print("Product :", FinalCalculator().product(3, 4))