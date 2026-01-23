try:
    with open("file.txt", "w") as f:
        f.write("Hello World")
        # print(f.read()) => we cannot do this here because the file is not yet opened in read mode
except FileNotFoundError:
    print("File not found")

try:
    with open("file.txt", "w") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
