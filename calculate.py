import sys
import math_lib as ml

try:
    a = sys.argv[1]
except:
    a = float(input("Set a ="))

try:
    b = sys.argv[2]
except:
    b = float(input("Set b ="))

print("Division of a by b:", ml.div(a, b))
print("Addition of a and b:", ml.add(a, b))
