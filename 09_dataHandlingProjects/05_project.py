import base64
import os

vault_file = "vault.txt"


def encode(text):
    encoded_text = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    return encoded_text


def decoded(text):
    decoded_text = base64.b64decode(text.encode("utf-8")).decode("utf-8")
    return decoded_text


def strength_checker(text):
    length = len(text)
    has_Uppercase = any(c.isupper() for c in text)
    has_digit = any(c.isdigit() for c in text)
    has_special_char = any(not c.isalnum() for c in text)

    score = sum([length, has_Uppercase, has_digit, has_special_char])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]


def add_credentials():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    strength = strength_checker(password)
    encoded_password = encode(password)
    with open(vault_file, "a") as f:
        f.write(f"{website},{username},{encoded_password},{strength}\n")

    print("Credentials added successfully")


def view_credentials():
    with open(vault_file, "r") as f:
        for line in f:
            try:
                website, username, encoded_password, strength = line.strip().split(",")
                password = decoded(encoded_password)
            except:
                continue
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"Strength: {strength}")
            print("-" * 20)


def main():
    if not os.path.exists(vault_file):
        with open(vault_file, "w") as f:
            f.write("website,username,password,strength\n")

    choice = input(
        "Enter 1 to view credentials\nEnter 2 to add credentials\nEnter 3 to exit\nEnter your choice: "
    )
    match choice:
        case "1":
            view_credentials()
        case "2":
            add_credentials()


if __name__ == "__main__":
    main()
