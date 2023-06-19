'''
Write a python code to validate URL using regular expression
'''

import re

def validate_url(url):
    pattern = re.compile(
        r'^(https?|ftp)://'  # Protocol (http, https, ftp)
        r'([A-Za-z0-9.-]+)'  # Domain (e.g., www.example.com)
        r'(:\d+)?'  # Optional port number (e.g., :8080)
        r'(/[A-Za-z0-9_\-/.]*)?'  # Optional path (e.g., /path/to/page)
        r'(\?[A-Za-z0-9_\-/.=&]*)?$'  # Optional query parameters (e.g., ?key=value&...)
    )

    if re.match(pattern, url):
        return True
    else:
        return False


# Example usage:
url1 = "https://www.example.com"
url2 = "ftp://ftp.example.com:8080/path/to/file"
url3 = "invalidurl"

print(validate_url(url1))  # True
print(validate_url(url2))  # True
print(validate_url(url3))  # False
