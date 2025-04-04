# errors and exceptions
# FileNotFound
# with open('dt.txt') as f:
#     f.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["apple", "banana", "Pear"]
# furit = fruit_list[3]


# TypeError
# text="abc"
# print(type+5)


# To handle exceptions

# try:
#     something that might cause an exception

# except:
#     do this if there was an exception
# else:
#     do this if there was no exception
# finally:
#     does this no matter what happens

try:
    file = open("a_file2.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} doesnot exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")


raise
