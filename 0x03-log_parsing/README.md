# 0x03. Log Parsing
For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

### Concepts Needed:
1) **File I/O in Python**: Understand how to read from sys.stdin line by line.
2) **Signal handling in Python**: Handling keyboard interrupt (CTRL + C) using signal handling in Python.
3) **Data Processing**: Parsing strings to extract specific data points and aggregating data to compute summaries.
4) **Regular expressions**: Using regular expressions to validate the format of each line.
5) **Dictionaries in Python**: Using dictionaries to count occurrences of status codes and accumulate file sizes.
6) **Exception handling**: Handling possible exceptions that may arise during file reading and data processing.

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A readme.md file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc


## Tasks
### 0. Log parsing
Write a script in python that reads `stdin` line by line and computes metrics:
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
- - Total file size: `File size: <total size>`
- - where <total size> is the sum of all previous <file size> 
- - number of lines by status code:
- - - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
- - - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
- - - format: `<status code>: <number>`
- - - status codes should be printed in ascending order

