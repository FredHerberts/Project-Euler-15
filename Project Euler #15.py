import math
import time
start = time.time()

a = math.factorial(40)
b = math.factorial(20)

print(a/(b*b))
end = time.time()
print(end - start)