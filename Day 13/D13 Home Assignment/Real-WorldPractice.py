import string_utils
# sentence = input("What is your sentence ? ")
# print(f"Total characters in your sentence are : {string_utils.count_character(sentence)} ")
# print(f"Total words in your sentence are : {string_utils.count_words(sentence)} ")
# print(f"Reverse of your sentence is : {string_utils.reverse_string(sentence)} ")


import shapes
# length = float(input("Enter the length of the Rectangle : "))
# breadth = float(input("Enter the breadth of the Rectangle : "))
# print(f"Area of Rectangle : {shapes.area_of_rectangle(length, breadth)}")

# radius = float(input("Ente the size of the radius of the Circle : "))
# print(f"Area of Circle : {shapes.area_of_circle(radius)}")

# side = float(input("Enter the size of the side of the square : "))
# print(f"Area of Square : {shapes.area_of_sqaure(side)}")


from config import HOST, PORT
# print("Settings - ")
# print(f"Host IP : {HOST}")
# print(f"Port : {PORT}")

import myproject.text_utils as text_utils
sentence = input("Ente a sentence : ")
print(f"Total vowels in your sentence are {text_utils.count_vowels(sentence)} ")
print(f"Total consonants in your sentence are {text_utils.count_consonants(sentence)} ")