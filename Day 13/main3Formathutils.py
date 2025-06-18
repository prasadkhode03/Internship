'''Create a Math Utility Package
Instructions:
Create a package mathutils/
Inside, create:
_init_.py
square.py → square(n)
cube.py → cube(n)
In main.py, import both and use them.
Add from .square import square in _init_.py
Then try: from mathutils import square'''

from mathutils.square import square
from mathutils.cube import cube
print("Square of 2 :", square(2))
print("Cube of 2 :", cube(2))