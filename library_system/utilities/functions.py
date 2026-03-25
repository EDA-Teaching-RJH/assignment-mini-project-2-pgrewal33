import re


def validate_isbn(isbn):
    pattern = r'^\d{3}-\d{3}-\d{3}$'
    return bool(re.match(pattern,isbn))

