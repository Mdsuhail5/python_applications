# def add(*args):
#     print(args[0])

#     for n in args:
#         sum += n
#     return sum


# print(add(4, 5, 6, 78, 8))


# *args is a many (ulimited) positon arguments
# **kargs is many keyword arguments
# the keyword arguments are stored in a dictionary with keyword as the key and the number as the value

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(n=2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissian")
print(my_car.make)
print(my_car.model)


# here for using **kwargs in class we use **kw in the constructor method
# pass the value for the args in instancation of the object
# if we call object.attribute it will get the value that has been passed
# if no value is passed error is thrown then we can use kw.get() to counter the error which provides none when the value is called
