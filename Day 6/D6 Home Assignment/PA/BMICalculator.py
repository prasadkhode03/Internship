#Part A: Functional Thinking
"""
2.	BMI Calculator
Define a function calculate_bmi(weight, height) that:
o	Takes weight in kg and height in meters
o	Calculates BMI: bmi = weight / (height ** 2)
o	Returns BMI and category:
	<18.5: Underweight
	18.5–24.9: Normal
	25–29.9: Overweight
	30+: Obese

"""

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Normal")
    elif bmi >= 25 and bmi <=29.9:
        print("Overweight")
    else:
        print("Obese")
    return bmi

weight = float(input("Enter your Weight (in kgs) : "))
height = float(input("Enter your Height (in meters : )"))
print("BMI =",calculate_bmi(weight, height))