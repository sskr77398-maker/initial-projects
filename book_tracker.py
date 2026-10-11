# import numpy as np


# contact_names = [  # ADD, DELETE, SEARCH, VIEW OR FOUND CONTACTS

#     {"name": "ron", "phone": 6299912500, "email": "ron@gmail.com123"},
#     {"name": "jane", "phone": 6300012501, "email": "jane@gmail.com456"},
#     {"name": "griffin", "phone": 640012502, "email": "griffin@gmail.com789"},
#     {"name": "james", "phone": 650012503, "email": "james@gmail.com012"}
# ]
'''enumerate() is a built-in Python function that lets you loop through a collection and get both the position (index) and value at the same time'''

# options = ["addccontact", "view_Contacts", "search_Contact", "delete contact", "exit"]

# while True:
#     print("\n--- CONTACT BOOK MENU ---")
#     for opt in options:
#         print(f"- {opt.title()}")

# if user == "exit":
#     print("Exiting the contact book. Goodbye!")
#     break

# if user == "add contact":
#     name = input("Enter name: ")
#     phone = input("Enter phone number: ")
#     email = input("Enter email: ")
#     contact_names.append({"name": name, "phone": phone, "email": email})
#     print("Contact added successfully!")

# elif user_choice == "view contacts":
#     for contact in contact_names:
#         print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}") 

# elif user_choice == "search contact":
#     pass           


# for option in options:
#     if option == "add contact":
#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")
#         email = input("Enter email: ")
#         contact_names.append({"name": name, "phone": phone, "email": email})
#         print("Contact added successfully!")

# for option in options:
#     if option == "view contacts":
#         for contact in contact_names:
#             print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# for option in options:
#     if option == "search contact":
#         search_name = input("enter name to search: ")
#         for contact in contact_names:
#             if contact["name"] == search_name:
#                 print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
#                 found = True
#                 break
#         else:
#             print("Contact not found!")

# for option in options:
#     if option == "delete contact":
#         delete_name = input("enter name of contact to delete: ")
#         for i, contact in enumerate(contact_names):
#             if contact["name"] == delete_name:
#                 del contact_names[i]
#                 print("Contact deleted successfully!")
#                 break
#         else:
#             print("Contact not found!")


import numpy as np

# Changed from parentheses () to brackets [] so it is a mutable list, 
# allowing you to append new contacts later.
contact_names = [
    {"name": "ron", "phone": "6299912500", "email": "ron@gmail.com123"},
    {"name": "jane", "phone": "6300012501", "email": "janu@gmail.com456"},
    {"name": "griffin", "phone": "640012502", "email": "griffin@gmail.com789"},
    {"name": "james", "phone": "650012503", "email": "james@gmail.com012"}
]

options = ["add contact", "view contacts", "search contact", "delete contact", "exit"]

while True:
    print("\n CONTACT BOOK MENU ")
    for opt in options:
        print(f" {opt.title()}")
        
    # 1. Ask the user what they want to do INSIDE the loop
    user_choice = input("\nChoose an option: ").lower().strip()
    
    # 2. Handle the "exit" option to break out of the infinite loop
    if user_choice == "exit":
        print("Goodbye!")
        break
        
    # 3. Check what the user selected and run the corresponding code
    if user_choice == "add contact":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_names.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!")
        
    elif user_choice == "view contacts":
        for contact in contact_names:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            
    elif user_choice == "search contact":
        pass
