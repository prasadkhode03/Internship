#🔹 Part B: Tuple Use Cases
'''6.	Store coordinates using a tuple:
location = (19.0760, 72.8777) (latitude, longitude)
o	Print each value separately.'''
location = (19.0760, 72.8777) #Tuple Packing
latitude, longitude = location #Tuple Unpacking
print("Latitude :", latitude)
print("Longitude :", longitude)


'''7.	Write a function get_min_max(numbers) that:
o	Accepts a list
o	Returns a tuple (min, max)'''

def get_min_max(numbers):
    maxi = max(numbers)
    mini = min(numbers)
    return (maxi, mini) #or  return (max(numbers), min(numbers))

demo_list = [15, 65, 231, 5, 656, 532]
max_min_tuple = get_min_max(demo_list)
print("Maximum and Minimum numbers (repectively) :",max_min_tuple) 