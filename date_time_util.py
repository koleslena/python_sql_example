from datetime import date, datetime
import random

_format_string = "%Y-%m-%d"

def calculate_age(adate):
    """
    Returns the total number of years as of today's date.

    Args:
        adate (date): The date to calculate.

    Returns:
        Age (int): the total number of years as of today's date.
    """
    today = date.today()
    age = today.year - adate.year
    return age - (1 if (today.month, today.day) < (adate.month, adate.day) else 0)

def check_date_format(date_string):
    """
    Returns True if the date string format matches the specified format, False otherwise.

    Args:
        date_string (string): The date string.

    Returns:
        True if the date string format matches the specified format, 
        False otherwise.
    """
    try:
        datetime.strptime(date_string, _format_string)
        return True
    except ValueError:
        return False

def to_str(adate):
    """
    Returns string format of a date within a specified format.

    Args:
        adate (date): The date to format.

    Returns:
        String format of the date.
    """
    return adate.strftime(_format_string)

def generate_random_birth_date(start_year, end_year):
    """
    Generates a random birth date within a specified year range.

    Args:
        start_year (int): The earliest year for the birth date.
        end_year (int): The latest year for the birth date.

    Returns:
        datetime.date: A randomly generated birth date.
    """
    if not (isinstance(start_year, int) and isinstance(end_year, int)):
        raise TypeError("start_year and end_year must be integers.")
    if start_year > end_year:
        raise ValueError("start_year cannot be greater than end_year.")

    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    return date(year, month, day)