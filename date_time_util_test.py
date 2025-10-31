from date_time_util import generate_random_birth_date, calculate_age, check_date_format, to_str
from datetime import date

def test_calculate_age():
    user_date = date(1990, 5, 15)
    assert calculate_age(user_date) == 35

    user_date = date(2000, 11, 29)
    assert calculate_age(user_date) == 24

def test_check_date_format():
    assert check_date_format('2000-04-12') == True
    assert check_date_format('12/03/2004') == False

def test_insert_batch_statement(): 
    assert to_str(date(2000, 11, 29)) == '2000-11-29'

def test_generate_random_birth_date():
    birth_date = generate_random_birth_date(1990, 2005)
    assert birth_date.year >= 1990
    assert birth_date.year <= 2005

