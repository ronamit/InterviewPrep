from typing import List, Dict, Tuple, Sequence
import itertools, collections


class Person:
    def __init__(self, Name: str, parentName=''):
        self.name = Name
        self.isAlive = True
        self.parentName = parentName
        self.childsNames = collections.deque()

    def add_child(self, childName):
        child = Person(childName, self.parentName)
        self.childsNames.appendleft(childName)  # add to start (queue is in increasing age order)
        return child


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.king = Person(kingName, '')
        self.persons = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.persons[parentName]
        child = parent.add_child(childName)
        self.persons[childName] = child


    def death(self, name: str) -> None:
        person = self.persons[name]
        person.isAlive = False
    # end def

    def getInheritanceOrder(self) -> List[str]:
        personName = self.kingName
        inhert_order_living = []
        # Run DFS
        stk = [personName]
        while stk:
            personName = stk.pop()
            person = self.persons[personName]
            if person.isAlive:
                inhert_order_living.append(person.name)
            # end if
            for childName in person.childsNames:
                stk.append(childName)
            # end for
        # end while
        return inhert_order_living
    # end def

# Your ThroneInheritance object will be instantiated and called as such:

t = ThroneInheritance("king")# order: king
t.birth("king", "andy")# order: king > andy
t.birth("king", "bob")# order: king > andy > bob
t.birth("king", "catherine")# order: king > andy > bob > catherine
t.birth("andy", "matthew")# order: king > andy > matthew > bob > catherine
t.birth("bob", "alex")# order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha")# order: king > andy > matthew > bob > alex > asha > catherine
inhert_order = t.getInheritanceOrder()# return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
print(inhert_order)
t.death("bob")# order: king > andy > matthew > bob > alex > asha > catherine
inhert_order = t.getInheritanceOrder()# return ["king", "andy", "matthew", "alex", "asha", "catherine"]
print(inhert_order)