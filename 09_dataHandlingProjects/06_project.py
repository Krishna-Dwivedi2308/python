# cryptographic fernet symmetric encryption

from cryptography.fernet import Fernet
from datetime import datetime
import os
import json

vault_file = "notes_vault.json"
key_file = "vault.key"

# ---------------- KEY HANDLING ----------------


def load_or_create_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        with open(key_file, "rb") as f:
            key = f.read()

    return Fernet(key)


fernet = load_or_create_key()

# ---------------- VAULT HANDLING ----------------


def load_vault():
    if not os.path.exists(vault_file):
        return []
    with open(vault_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_vault(data):
    with open(vault_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------------- FEATURES ----------------


def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({"title": title, "content": encrypted_content, "timestamp": timestamp})

    save_vault(data)
    print("Note added successfully!")


def list_notes():
    data = load_vault()
    if not data:
        print("No notes yet")
        return

    for i, note in enumerate(data, start=1):
        print(f'{i}. {note["title"]} ({note["timestamp"]})')


def view_note():
    list_notes()
    try:
        index = int(input("Enter note number to view: ")) - 1
        data = load_vault()
        if 0 <= index < len(data):
            encrypted = data[index]["content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"\n{data[index]['title']} - {data[index]['timestamp']}\n")
            print(decrypted)
        else:
            print("Invalid input")
    except Exception as e:
        print("Invalid input")


# ---------------- MAIN LOOP ----------------


def main():
    while True:
        print("\n1. Add note")
        print("2. List notes")
        print("3. View note")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


main()
