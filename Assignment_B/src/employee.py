# Install first:
# pip install pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create Database
db = client["employee_db"]

# Create Collection
collection = db["employees"]


# CREATE
def create_data():
    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    data = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    result = collection.insert_one(data)
    print("Employee Data Inserted Successfully")
    print("ID:", result.inserted_id)


# READ
def read_data():
    print("\nEmployee Records:\n")

    for data in collection.find():
        print("ID:", data["_id"])
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Department:", data["department"])
        print("Salary:", data["salary"])
        print("----------------------")


# UPDATE
def update_data():
    id = input("Enter Employee ID to Update: ")

    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_department = input("Enter New Department: ")
    new_salary = float(input("Enter New Salary: "))

    collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": new_name,
                "age": new_age,
                "department": new_department,
                "salary": new_salary
            }
        }
    )

    print("Employee Data Updated Successfully")


# DELETE
def delete_data():
    id = input("Enter Employee ID to Delete: ")

    collection.delete_one(
        {"_id": ObjectId(id)}
    )

    print("Employee Data Deleted Successfully")


# MENU
while True:
    print("\n--- EMPLOYEE CRUD MENU ---")
    print("1. Insert")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_data()

    elif choice == "2":
        read_data()

    elif choice == "3":
        update_data()

    elif choice == "4":
        delete_data()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")