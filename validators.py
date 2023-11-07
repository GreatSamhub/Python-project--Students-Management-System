import re

def validate_name(name):
    """Validate a name to contain only letters and spaces."""
    if not re.match(r'^[A-Za-z\s]+$', name):
        raise ValueError("Name should contain only letters and spaces.")

def validate_integer(input_value):
    """Validate an input to be a valid integer."""
    try:
        int(input_value)
    except ValueError:
        raise ValueError("Input should be a valid integer.")


