from dataclasses import dataclass, field
from itertools import  count
import attr
import random

#https://stackoverflow.com/questions/71195208/creating-a-unique-id-in-a-python-dataclass
# 
# 
# https://docs.python.org/3/library/dataclasses.html
# https://bobbyhadz.com/blog/python-create-incremental-id-in-class


@dataclass()
class Person():
    _id : int = field(default_factory=count().__next__)
    name : str
    age : int 
    pass

NAMES = ["Arvid","Bent","Sivert","Leo"]

ppl = []
for i in range(10):
    p = Person()
    p.name = random.choice(NAMES)
    p.age = random.randint(18,48)
    ppl.append(p)



class Mercenary(Person):
    """Cant be passed ID """
    #id : int = attr(field(default_factory=count().__next__ , init=False))
    pass


