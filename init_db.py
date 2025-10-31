import psycopg2
from psycopg2 import extras

from benchmark import benchmark

class DB:
    _conn = None

    def connect(self):
        """Creates a connection to the database."""
        if not self._conn or self._conn.closed:
            self._conn = psycopg2.connect("dbname=db_test user=ht password=ht host=localhost port=5432")

    def close_connection(self):
        """Closes the connection to the database."""
        if self._conn:
            self._conn.close()

    @benchmark
    def execute_query(self, command):
        """Executes the query."""
        res = []
        try:
            self.connect()  
            with self._conn.cursor() as cursor:
                cursor.execute(command)
                res = cursor.fetchall()
        except Exception as err:
            print(f"Command skipped: {command}, {err}")
        finally:
            self.close_connection()
        return res

    def execute_command(self, command):
        """Executes the command."""
        try:
            self.connect()
            with self._conn.cursor() as cursor:
                cursor.execute(command)
            self._conn.commit()
        except Exception as err:
            print(f"Command skipped: {command}, {err}")
        finally:
            self.close_connection()

    def execute_batch_insert(self, sql, data):
        """Performs insertion of a data batch."""
        batch_size = 100000
        data_len = len(data)
        try:
            self.connect()
            with self._conn.cursor() as cursor:
                for i in range(data_len//batch_size + 1):
                    extras.execute_batch(cursor, sql, data[i*batch_size: min((i + 1)*batch_size, data_len)])
            self._conn.commit()
        except Exception as err:
            print(f"Command skipped: {sql}, {err}")
        finally:
            self.close_connection()
    
    def execute_list_commands(self, commands):
        """Executes a list of commands."""
        try:
            self.connect()
            with self._conn.cursor() as cursor:
                for command in commands:
                    cursor.execute(command)
                self._conn.commit()
        except Exception as err:
            print(f"Command skipped: {commands}, {err}")
        finally:
            self.close_connection()

    def is_initialized(self):
        """Checks if tables have been created in the database."""
        try:
            self.connect()
            res = self.execute_command("""
                    SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE  table_schema = 'ht'
                    AND    table_name   = 'users'
                    );
                                    """)
            
            return res[0][0]
        except:
            return False
        finally:
            self.close_connection()

    def initialize_database(self, filename='init_db.sql'):
        """Initializing the database, creating tables."""
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.replace('\t', '').replace('\n', '').split(';')

        self.execute_list_commands(sqlCommands[:-1])
        
    