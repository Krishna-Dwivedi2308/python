import os
import shutil

extension_map = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf"],
    "Audio": [".mp3", ".wav", ".ogg"],
    "Video": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in extension_map.items():
        if ext in extensions:
            return folder

    return "others"


def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)
            os.makedirs(dest_path, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved {file} => {dest_folder}")


if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank").strip()
    print(type(folder))
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid Directory")
    else:
        sort_files(folder)
        print("Sorting completed")
