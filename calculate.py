import math_lib as ml
import sys

try:
    a = int(sys.argv[1])
except:
    a = int(input("Enter first value:\n"))

try:
    b = int(sys.argv[2])
except:
    b = int(input("Enter second value:\n"))

print(a, "divided by", b, "=", ml.div(a,b))
print(a, "plus", b, "=", ml.add(a,b))

