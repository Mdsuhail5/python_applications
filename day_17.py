class User:
    def __init__(self, user_id, username):
        self.id = user_id  # object.attribute=attribute value
        self.username = username
        self.followers = 0
        self.following = 0

    # when a method is called it should have self parameter, so that it knows the object that called it.
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Dave")
user_2 = User("001", "Dave")

print(user_1.username)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
# class passcal case
# instance snake case
# class is a blueprint
# instance is a copy of the class
# object is a concrete entity that has both data and behaviour , it is based on crating a class, which defines the blueprint of the object
# instance is the realization of the object i.e when you are creating an object from a class you are instantiating the class, which means creating an instance of that class.
# attribute is the variable attached to an object eg user1.id where id is the attributes

# constructor
