black_tea_grams = 14
ginger_grams = 3
total_grams = black_tea_grams + ginger_grams
print(total_grams)  # 17

milk = 7
servings = 4
milk_per_serving = milk / servings
print(milk_per_serving)  # 1.75 => decimal part is preserved

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(bags_per_pot)  # 1 => decimal part is discarded

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(leftover_pods)  # 1 => remainder given here .

# OUTPUT
# 17
# 1.75
# 1
# 1

# ** for exponent. 2**3 = 8
# also for readability it , lets you write 1 billion as 1_000_000_000 , it will be read as 1000000000 internally.
billion = 1_000_000_000
print(billion)  # 1000000000

isboiling = True
print(isboiling)  # True
total = 9 + isboiling  # upcasting
print(total)  # 10
print(bool(total))  # True

# and, or , not

# membership operator
# in , not in

# identity operator
# is , is not

# we also have support of libs for different specific use cases
import sys
from fractions import Fraction
from decimal import Decimal
import sys

# Purpose: Interact with the Python interpreter and runtime environment.

# Used for:
# Access command-line arguments (sys.argv)
# Exit a program (sys.exit())
# Get Python version (sys.version)
# Work with input/output streams (sys.stdin, sys.stdout)
# 👉 Think of sys as Python talking to the system.

# from fractions import Fraction
# Purpose: Work with exact rational numbers (fractions).
# Used for:
# Representing numbers like 1/3 exactly (no floating-point error)
# Performing precise fraction arithmetic
# Fraction(1, 3) + Fraction(1, 6)  # = 1/2
# 👉 Use when precision matters and floats are inaccurate.

# from decimal import Decimal
# Purpose: Perform high-precision decimal arithmetic.
# Used for:
# Financial calculations
# Avoiding floating-point rounding issues
# Controlling precision explicitly
# Decimal("0.1") + Decimal("0.2")  # = 0.3 (exact)
# 👉 Use for money and scientific precision, not speed.
# One-line summary
# sys → system-level interaction
# Fraction → exact rational math
# Decimal → precise decimal math
# If you want, I can also explain when to use float vs Decimal vs Fraction with real-world examples.
