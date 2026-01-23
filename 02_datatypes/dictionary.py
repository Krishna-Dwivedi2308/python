chai_order = {"type": "chai", "size": "large", "sugar": 5}
print(chai_order)
print(chai_order["size"])
print(type(chai_order))

student = dict(roll_no=1, name="abc", marks=90)

print("data type", type(student))
print("intial dict:\n", student)
student["gender"] = "male"
print("after adding new key\n", student)
del student["gender"]
print("after deleting key", student)
print(student.keys(), student.values(), student.items(), sep="\n")

last_item = student.popitem()
print(last_item)
print(student)

# what is the best way to safely access the value of a key that may or may not exist in a dictionary?
print(student.get("roll_no", "not found"))
print(student.get("age", "not found"))

# all union , intersection , difference , membership are valid in dictionary as well as they were in sets .
