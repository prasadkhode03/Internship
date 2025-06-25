#🌟 Part C: Static Methods for General Operations
'''5.	Math Helper Class
o	Create a class MathHelper with static methods:
	is_prime(num) – Returns True if the number is a prime.
	gcd(a, b) – Returns the greatest common divisor.
	lcm(a, b) – Returns the least common multiple.
o	Test with different inputs.'''
class MathHelper:
    @staticmethod
    def is_prime(num):
        if num % 2 == 0:
            return True
        else:
            return False
        
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a, b):
        return (a * b) // MathHelper.gcd(a, b)
    
helper = MathHelper()
print("Is 5 Prime ? :", helper.is_prime(5))
print("GCD of 42 and 18 :", helper.gcd(42, 18))
print("LCM of 10 and 6 :", helper.lcm(10, 6))

