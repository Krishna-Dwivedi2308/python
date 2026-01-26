Great topic — `json` is one of the **most used standard libraries in Python**.

I’ll teach it in a **structured, practical way**:
what each function does, when to use it, and how they differ.

---

# What is the `json` module?

> The `json` module is used to **convert between Python objects and JSON data**.

Two directions:

* Python → JSON (serialization)
* JSON → Python (deserialization)

---

# Core Functions in `json`

These are the **4 main functions you must know**:

| Function       | Direction            | Purpose                     |
| -------------- | -------------------- | --------------------------- |
| `json.dumps()` | Python → JSON string | Convert object to JSON text |
| `json.loads()` | JSON string → Python | Parse JSON text             |
| `json.dump()`  | Python → JSON file   | Write JSON to file          |
| `json.load()`  | JSON file → Python   | Read JSON from file         |

---

## 1. `json.dumps()` (object → string)

```python
import json

data = {"tea": "masala", "sugar": 2}
json_str = json.dumps(data)
print(json_str)
```

Output:

```json
{"tea": "masala", "sugar": 2}
```

### Use when:

* Sending data over network
* APIs
* Logging
* Storing in DB

---

## 2. `json.loads()` (string → object)

```python
json_str = '{"tea": "masala", "sugar": 2}'
data = json.loads(json_str)
print(data)
```

Output:

```python
{'tea': 'masala', 'sugar': 2}
```

### Use when:

* Reading API responses
* Parsing config
* Processing JSON text

---

## 3. `json.dump()` (object → file)

```python
with open("chai.json", "w") as f:
    json.dump(data, f)
```

Writes JSON into file.

---

## 4. `json.load()` (file → object)

```python
with open("chai.json") as f:
    data = json.load(f)
```

Reads JSON file into Python dict.

---

# Important Optional Parameters (Real World)

These make `json` powerful.

---

## `indent` (pretty print)

```python
json.dumps(data, indent=4)
```

Readable formatted JSON.

---

## `sort_keys`

```python
json.dumps(data, sort_keys=True)
```

Sorts keys alphabetically.

---

## `ensure_ascii`

```python
json.dumps("चाय", ensure_ascii=False)
```

Allows Unicode characters.

---

## `default` (custom objects)

```python
def serialize(obj):
    return obj.__dict__

json.dumps(obj, default=serialize)
```

Used for:

* Classes
* Datetime
* Complex objects

---

# Supported Data Types

JSON can handle:

| Python     | JSON       |
| ---------- | ---------- |
| dict       | object     |
| list       | array      |
| str        | string     |
| int/float  | number     |
| True/False | true/false |
| None       | null       |

Not supported:

* set
* tuple
* custom objects (without `default`)

---

# json vs pickle (important)

| Feature           | json | pickle |
| ----------------- | ---- | ------ |
| Human readable    | ✅    | ❌      |
| Secure            | ✅    | ❌      |
| Cross-language    | ✅    | ❌      |
| Can store classes | ❌    | ✅      |
| Used in APIs      | ✅    | ❌      |

---

# Mental Model 🧠

Think of `json` as a **translator**:

```
Python objects  ⇄  JSON text
```

Used whenever:

* Python talks to web
* Python talks to frontend
* Python stores structured data

---

# Internal Architecture (important)

`json` internally:

* Tokenizes text
* Builds parse tree
* Maps JSON types to Python types
* Serializes objects recursively

It is a **parser + serializer**.

---

# Real World Usage Patterns

### API response

```python
response = requests.get(url)
data = response.json()
```

### Config files

```python
config = json.load(open("config.json"))
```

### Database storage

```python
db.save(json.dumps(obj))
```

---

# Complete Function Index (json module)

| Function      | Purpose              |
| ------------- | -------------------- |
| `dumps()`     | Object → JSON string |
| `loads()`     | JSON string → object |
| `dump()`      | Object → file        |
| `load()`      | File → object        |
| `JSONEncoder` | Custom encoding      |
| `JSONDecoder` | Custom decoding      |

(Last two are advanced, used for frameworks)

---

# One-line Interview Takeaway (Gold)

> **The `json` module serializes Python objects into JSON and deserializes JSON back into Python, enabling data exchange between systems.**

---

# Final Key Insight

If you understand `json`, you understand:

* REST APIs
* Microservices
* Frontend-backend communication
* Config systems
* Cloud systems

This is **not optional knowledge** — it is **core software engineering skill**.
