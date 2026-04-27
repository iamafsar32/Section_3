# Install first:
# pip install pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create Database
db = client["student_db"]

# Create Collection
collection = db["students"]


# CREATE
def create_data():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")

    data = {
        "name": name,
        "age": age,
        "city": city
    }

    result = collection.insert_one(data)
    print("Data Inserted Successfully")
    print("ID:", result.inserted_id)


# READ
def read_data():
    print("\nStudent Records:\n")

    for data in collection.find():
        print("ID:", data["_id"])
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("City:", data["city"])
        print("----------------------")


# UPDATE
def update_data():
    id = input("Enter Student ID to Update: ")

    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_city = input("Enter New City: ")

    collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": new_name,
                "age": new_age,
                "city": new_city
            }
        }
    )

    print("Data Updated Successfully")


# DELETE
def delete_data():
    id = input("Enter Student ID to Delete: ")

    collection.delete_one(
        {"_id": ObjectId(id)}
    )

    print("Data Deleted Successfully")


# MENU
while True:
    print("\n--- CRUD MENU ---")
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