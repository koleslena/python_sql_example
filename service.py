import names

from init_db import DB
from user import User
from benchmark import benchmark
from date_time_util import generate_random_birth_date

class Service:
    def __init__(self):
        self.db = DB()

    def initialise(self):
        if not self.db.is_initialized():
            self.db.initialize_database()

    def insert_user(self, name, date, gender):
        user = User(name, date, gender[0])
        self.db.execute_command(user.insert_statement())

    def insert_batch(self, data):
        sql = User.insert_batch_statement()
        self.db.execute_batch_insert(sql, data)

    @benchmark
    def select_users(self, start_name, gender):
        sql = User.select_statement(start_name, gender)
        data = self.db.execute_query(sql)
        return [User(elem[0], elem[1], elem[2]) for elem in data]
    
    def select_all_users(self):
        sql = User.select_all_statement()
        data = self.db.execute_query(sql)
        return [User(elem[0], elem[1], elem[2]) for elem in data]
    
    def generate_users(self, num):
        specified_num = 100000
        males = [(names.get_full_name(gender='male'), generate_random_birth_date(1950, 2005), 'M') for _ in range(num//2)]
        females = [(names.get_full_name(gender='female'), generate_random_birth_date(1950, 2005), 'F') for _ in range(num//2)]
        specified = [(f"F{names.get_full_name(gender='male')}", generate_random_birth_date(1950, 2005), 'M') for _ in range(specified_num)]
        sql = User.insert_batch_statement()
        self.db.execute_batch_insert(sql, males + females + specified)
