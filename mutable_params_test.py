# coding: utf-8
# @Time: 2019-07-24 18:16
# @Author: 'haifeng.shi@klook.com'

class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers=passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


print('default',HauntedBus.__init__.__defaults__)
bus1=HauntedBus(['Alice', 'Bill'])
print('default',HauntedBus.__init__.__defaults__)
print(bus1.passengers)
bus1.pick('Charlie')
print('default',HauntedBus.__init__.__defaults__)
bus1.drop('Alice')
print('default',HauntedBus.__init__.__defaults__)
print(bus1.passengers)


from collections import Sequence
from collections import OrderedDict