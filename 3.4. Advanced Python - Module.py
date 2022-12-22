print("=====MODULE=====") # Module concept using if we want break one large python file into smaller parts
print("=====CREATE OWN MODULE=====")

import playvideo as pv
# from playvideo import*

# from playvideo import GENRE, DURATION, LANGUAGE # just take for using few statement


print(pv.GENRE)

print(pv.DURATION)

pv.play("John Wick 3")

print("\n=====BUILT-IN MODULE=====")
# module default in python
import os
import math

from math import pi
from math import e

print(pi)
print(e)

# Goal Module for manageable and reusable