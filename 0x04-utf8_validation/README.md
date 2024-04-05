# 0x04. UTF-8 Validation
For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding. Here’s a list of concepts and resources that will be helpful:

## Concepts Needed:
1. **Bitwise Operations in Python**: Understanding how to manipulate bits in python, including operations like AND, OR, XOR, NOT and, shifts.

2. **UTF-8 Encoding scheme**: Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.

3. **Data representation**: How to represent and work with data at the byte level.

4. **List manipulation in python**: Iterating through lists, accessing list elements, and understanding list comprehensions.

5. **Boolean logic**: Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

## Learning
UTF-8 is a text encoding standard used for electronic communication. It stands for Unicode Transformation Format - 8 bit. The UTF-8 is capable of encoding code points to one to four bytes depending on the value of the code point.

| First code point | Last code point | Byte 1   | Byte 2   | Byte 3   | Byte 4   |
| ---------------- | --------------- | -------- | -------- | -------- | -------- |
| U + 0000         | U + 007F        | 0xxxxxxx |          |          |          |
| U + 0080         | U + 07FF        | 110xxxxx | 10xxxxxx |          |          |
| U + 0800         | U + FFFF        | 1110xxxx | 10xxxxxx | 10xxxxxx |          |
| U + 010000       | U + 10FFFF      | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |

The first 128 code points (ASCII) which is U+ 0000 to U+007F need 1 byte. This corresponds to languages that use the latin alphabet like English, French and Spanish.

The next 1920 code points need two bytes to code that is from U+0000 to U+07FF. This corresponds to the languages that use the latin script but with accents and special characters like Greek, Coptic, Cyrillic, Armenian, Hebrew and Arabic.

Three bytes are required for languages like Chinese, Japanese and Korean. And finally four bytes for emoji representations and mathematical notations. 

**Example 1:**

**Input:** data = [197,130,1]

**Output:** true

**Explanation:** data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

---

**Example 2:**

**Input:** data = [235,140,4]

**Output:** false

**Explanation:** data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

---

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
