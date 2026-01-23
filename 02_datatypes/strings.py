# note that strings are 'immutable' 

str1="hello"
print(str1)
print(id(str1))

str1="world"
print(str1)
print(id(str1))
# hello
# 2769356151408
# world
# 2769356376512

print(str1[0]) #w
print(str1[1]) #o
print(str1[2]) #r
print(str1[3]) #l
print(str1[4]) #d
# print(str1[5]) #error
print(str1[0:5]) # world - because the last letter is not inclusive in python like this so we add one more index number so that it prints till the prev index number

print(str1[::-1]) #this will print the string in reverse directly

# ------------------------------------
# ENCODING AND DECODING
# ------------------------------------

str1="hello"
print(str1) #hello
print(type(str1)) # <class 'str'>
print(id(str1)) # 2374807738992

str1=str1.encode("utf-8")
print(str1) # b'hello'
print(type(str1)) # <class 'bytes'>
print(id(str1)) # 2769356376512

str1=str1.decode("utf-8")
print(str1) # hello
print(type(str1)) # <class 'str'>
print(id(str1)) # 2374807967792
print(id('hello')) # 2374807738992
print(id('hello')==id(str1)) # False

# Concise Summary

# Strings are immutable in Python. Any operation that seems to “modify” a string actually creates a new object.

# In the code:
# "hello" → a str object (often interned).
# .encode("utf-8") → creates a new bytes object → id changes.
# .decode("utf-8") → creates a new str object → id changes again.
# Even though the decoded string has the same value ("hello"), it is not the same object as the original literal.
# Why id('hello') != id(str1) after decoding
# 'hello' in code is a string literal and is usually interned (stored once in a global string pool).
# decode() creates a runtime string, which Python does not auto-intern.

# Result:
# str1 == 'hello' → True (same value)
# # str1 is 'hello' / id(str1) == id('hello') → False (different objects)

# Interning (key concept)
# Interning = Python stores one shared copy of certain immutable objects (mainly string literals and small integers) and reuses it.
# Benefits: less memory, faster comparisons.

# Automatic interning:
# String literals, identifier-like strings
# Small integers -5 to 256
# Runtime-created strings are not automatically interned.
# You can force it with:
# import sys
# str1 = sys.intern(str1)

# Final takeaways
# Encoding/decoding always creates new objects.
# Same value ≠ same object (== vs is).
# Interning is an optimization, not something to rely on in logic.