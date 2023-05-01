import os
import random
import string

file_name = "****.txt"

if os.path.isfile(file_name):
    user_input = input("The file already exists. Do you want to continue? (y/n): ")
    if user_input.lower() != "y":
        print("You do not have the permission to execute this file.")
        os.remove(__file__)
        exit()
    else:
        print("Executing the file...")

else:
    print("File does not exist. Overwriting and deleting this file...")
    new_content = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))
    with open(file_name, "w") as f:
        f.write(new_content)
    os.remove(__file__)
