from date_time_util import to_str, calculate_age

class User:
    _table_name = 'users'
    _insert_sql = f"INSERT INTO {_table_name} (full_name, date_of_birth, gender) VALUES ('{{}}', '{{}}', '{{}}');"
    _insert_batch_sql = f"INSERT INTO {_table_name} (full_name, date_of_birth, gender) VALUES ({{}}, {{}}, {{}});"
    _select_sql = f"SELECT full_name, date_of_birth, gender FROM {_table_name} where {{}};"
    _select_all_sql = f"SELECT DISTINCT ON (full_name, date_of_birth) full_name, date_of_birth, gender FROM {_table_name} ORDER BY full_name;"

    def __init__(self, full_name, date_of_birth, gender):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
    
    def age(self):
        return calculate_age(self.date_of_birth)

    def insert_statement(self):
        return self._insert_sql.format(self.full_name, self.date_of_birth, self.gender)

    def insert_batch_statement():
        return User._insert_batch_sql.format('%s', '%s', '%s')
    
    def select_statement(start_name, gender):
        return User._select_sql.format(f"gender = '{gender}' and full_name like '{start_name}%'")
    
    def select_all_statement():
        return User._select_all_sql
    
    def __str__(self):
        return f"""User: full_name='{self.full_name}', \
                        birth_date={to_str(self.date_of_birth)}, \
                        gender={'Male' if self.gender == 'M' else 'Female'}, \
                        age={self.age()}"""

