"""Examples runner."""


import sys


from .units import *
from .one_of_each import *


function_name = sys.argv[1]


locals()[function_name]()
