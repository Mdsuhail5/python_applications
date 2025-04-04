# type hinting is new feature in python
# it allows us to set the data type before intalizing the value of the variable
# a : int
# the variables can be intialized afterwards and gives warning if the data is any other type
# a : int -> str     here the arrow shows the output of the func should be of the mentioned datatype

def police_check(age: int) -> bool:
    if age < 18:
        can_drive = False
    else:
        can_drive = True
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine")
