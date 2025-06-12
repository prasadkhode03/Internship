#🔹 Part D: List Comprehension

#11. Create a list of squares from 1 to 10 using list comprehension.
#Example: [1, 4, 9, ..., 100]
square_list = [i ** 2 for i in range(1, 10+1)]
print("List of squares upto 10 :",square_list)


#12. From a list of numbers 1 to 20, create a new list that contains only even numbers using list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even = [num for num in numbers if num % 2 == 0]
print("\nEven Numbers List :", even)


#13. Given words = ["Apple", "banana", "Cherry"], create a new list with all words in lowercase using list comprehension. (hint: use lower())
words = ["Apple", "banana", "Cherry"]
lower_list = [word.lower() for word in words]
print("Lower Case List :", lower_list)


#14. From a string "python", create a list of characters using list comprehension.
string = "python"
characters = [char for char in string]
print("Character :",characters)


#15. Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.
divisible_list = [num for num in range(1, 50+1) if num % 3 == 0 and num % 5 == 0]
print("Divisible List :", divisible_list)