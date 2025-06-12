'''Part A: Functional Thinking
1.	Greeting Based on Time
Define a function greet_user(hour) that:
o	Takes current hour (24-hr format)
o	Prints:
	"Good Morning" if 5–12
	"Good Afternoon" if 12–17
	"Good Evening" if 17–21
	"Good Night" otherwise'''

def greet_user(hour):
    if hour >= 5 and hour <= 12:
        print("Good Morning")
    elif hour > 12 and hour <= 17:
        print("Good Afternoon")
    elif hour > 17 and hour <=21:
        print("Good Evening")
    else:
        print("Good Night")

hour = int(input("Enter current hour (24 hr format) : "))
greet_user(hour)
