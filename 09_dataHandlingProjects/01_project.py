import csv
import os

filename = "contacts.csv"

if not os.path.exists(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["First Name", "Last Name", "Phone Number", "Email Address"])


def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address: ")
    # check for duplicates before adding
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == first_name and row[1] == last_name:
                print("Contact already exists!")
                return

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([first_name, last_name, phone_number, email_address])
    print("Contact added successfully!")


def view_contacts():
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search_contact():
    search_term = input("Enter search term: ")
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if search_term in row:
                print(row)
            else:
                print("Contact not found!")


def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
