import re


def validate_isbn(isbn):
    format = r'^\d{3}-\d{3}-\d{3}$'
    return bool(re.match(format,isbn))

def validate_year(year):
    format = r'^\d{4}$'
    if not re.match(format, str(year)):
        return False
    return 1900 <= int(year) <= 2026

def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return [int(n) for n in numbers]