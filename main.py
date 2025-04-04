import os


# Specify the directory name
for n in range(28, 101):
    directory_name = f"day_{n}"
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

# all the directories were created using this code
