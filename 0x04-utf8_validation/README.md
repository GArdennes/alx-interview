# 0x04. UTF-8 Validation
For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:

## Concepts Needed:
1. **Bitwise Operations in Python**: Understanding how to manipulate bits in python, including operations like AND, OR, XOR, NOT and, shifts.

2. **UTF-8 Encoding scheme**: Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.

3. **Data representation**: How to represent and work with data at the byte level.

4. **List manipulation in python**: Iterating through lists, accessing list elements, and understanding list comprehensions.

5. **Boolean logic**: Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using `python3`.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A readme file, at the root of the folder of the project, is mandatory.
- Your code should use the `PEP 8` style.
- All your files must be executable.


## Tasks
### 0. UTF-8 Validation
Write a method that determines if a given dataset represents a valid UTF-8 encoding.
- Prototype: `def validUTF8(data)`
- Return: `True` if data is valid UTF-8 encoding,  else return `False`.
- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.
