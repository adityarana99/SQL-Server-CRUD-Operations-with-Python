import pyodbc


class SqlCRUD:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = f"DRIVER=SQL SERVER NATIVE CLIENT 11.0;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
            self.cursor = self.connection.cursor()
            print("Connected to the database successfully.")
        except Exception as e:
            print("Error occurred while connecting to the database:", e)

    def create_record(self, table_name, values):
        try:
            query = f"insert into {table_name} (CustomerName, CustomerAge, CustomerLocation) values(?, ?, ?)"
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print("Error occurred while inserting record:", e)

    def read_record(self, table_name):
        try:
            query = f"select * from {table_name}"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            for n in results:
                print(n)
        except Exception as e:
            print("Error occurred while reading records:", e)

    def update_record(self, table_name, update_values, update_condition):
        try:
            query = f"update {table_name} set CustomerName=?, CustomerAge=?, CustomerLocation=? where {update_condition}"
            self.cursor.execute(query, update_values)
            self.connection.commit()
            print("Record updated successfully.")
        except Exception as e:
            print("Error occurred while updating record:", e)

    def delete_record(self, table_name, delete_condition):
        try:
            query = f"delete from {table_name} where {delete_condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print("Record deleted successfully.")
        except Exception as e:
            print("Error Occurred while deleting record:", e)

    def disconnect(self):
        try:
            self.connection.close()
            print("Disconnected from the database.")
        except Exception as e:
            print("Error occurred while disconnecting from the database:", e)
