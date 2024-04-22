import math
import sys
import time

sys.set_int_max_str_digits(48000)

start = time.time()

x = math.factorial(10000)
print(x)

end = time.time()
print(end - start)