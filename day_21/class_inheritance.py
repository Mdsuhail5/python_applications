# class inheritance: the process of inherting behaviour and appearance from an existing class

class Animal:

    def __init__(self):
        self.eyes = 2

    def breath(self):
        print('inhale, exhale')


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print('doing this underwater.')

    def swim(self):
        print('moving in water.')


fish = Fish()
print(fish.eyes)
fish.swim()
fish.breath()
