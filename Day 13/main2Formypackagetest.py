'''Create and Use a Simple Package
Goal: Learn basic package structure and importing.
Instructions:
Create a directory called mypackage/
Inside it, create:
_init_.py (can be empty)
greet.py with a function say_hello(name) that returns "Hello, <name>!"
In main.py (outside mypackage):
Import and call say_hello("Alice")
Check: Does main.py run correctly and print the greeting?'''


from mypackage import greet
greet.say_hello("Prasad")

#OR  from mypackage.greet import say_hello
# say_hello("Prasad")







