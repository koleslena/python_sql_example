from user import User
from datetime import date

def test_age():
    user = User('FIO', date(1990, 5, 15), 'M')
    assert user.age() == 35

    user = User('FIO', date(2000, 11, 29), 'F')
    assert user.age() == 24

def test_insert_statement():
    user = User('FIO', date(2000, 11, 29), 'F')
    assert user.insert_statement() == "INSERT INTO users (full_name, date_of_birth, gender) VALUES ('FIO', '2000-11-29', 'F');"

def test_insert_batch_statement(): 
    assert User.insert_batch_statement() == "INSERT INTO users (full_name, date_of_birth, gender) VALUES (%s, %s, %s);"

def test_select_statement():
    assert User.select_statement('F', 'M') == "SELECT full_name, date_of_birth, gender FROM users where full_name like 'F%' and gender = 'M';"