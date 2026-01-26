# this is a code to flatten json using recursion in python

import json
import os

input_file = "nested_data.json"
output_file = "flattened_data.json"


def flatten_json(data, sep=".", parent_key=""):
    items = {}
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = (
                f"{parent_key}{sep}{key}" if parent_key else key
            )  # here we create the key for nested dicts
            # print(full_key)
            items.update(flatten_json(value, sep=sep, parent_key=full_key))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            # print(full_key)
            items.update(flatten_json(item, sep, full_key))
    else:
        items[parent_key] = data
        print(items)
    return items


def main():
    if not os.path.exists(input_file):
        print("No file found")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        sep = input("enter your seperator").strip() or "."
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(flatten_json(data, sep=sep), f, indent=2)
        print(f"converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Following error occured : {e}")


if __name__ == "__main__":
    main()
