# Explicit actions: define a fuction with the same name in Child
class Parent(object):
    
    def override(self):
        print "PARENT override()"

class Child(Parent):
    
    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
