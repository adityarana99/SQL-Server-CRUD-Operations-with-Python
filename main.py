
from SQLServerDB import SqlCRUD


def main():
    server = 'DESKTOP-E0FLFBP\ADITYASQL'
    database = 'PythonSQLInteractionDemo'
    username = 'sa'
    password = 'Password@2809'

    db = SqlCRUD(server, database, username, password)
    db.connect()

    table_name = "Customers"

    while True:
        print("\nSelect an option:")
        print("1. Create a record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit\n")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter CustomerName: ")
            age = input("Enter CustomerAge: ")
            location = input("Enter CustomerLocation: ")
            db.create_record(table_name, (name, age, location))

        elif choice == "2":
            print("\nAll Records:")
            db.read_record(table_name)

        elif choice == "3":
            name = input("Enter CustomerName: ")
            age = input("Enter CustomerAge: ")
            location = input("Enter CustomerLocation: ")
            update_condition = input("Enter condition for update (e.g., CustomerID=1): ")
            db.update_record(table_name, (name, age, location), update_condition)

        elif choice == "4":
            delete_condition = input("Enter condition for delete (eg., CustomerID=1): ")
            db.delete_record(table_name, delete_condition)

        elif choice == "5":
            db.disconnect()
            print("Thank you for using this service. And the connection has been closed")

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()

