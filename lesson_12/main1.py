from classwork_01 import create_connection

if __name__ == "__main__":
    result = create_connection()
    if result:
        print("Database created")
    else:
        print("Database already exists")
