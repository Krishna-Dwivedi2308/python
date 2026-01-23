# ------------------------
# walrus operator :=
# ------------------------

value=13
reamineder=value%2

if reamineder == 0:
    print("even number")
else:
    print("odd number")

# now same program using wlarus operator

value=13

if (reamineder := value%2) == 0: # walrus operator lets you assign a value to a variable at the same time as you're testing it in a condition
    print("even number")
else:
    print("odd number")

