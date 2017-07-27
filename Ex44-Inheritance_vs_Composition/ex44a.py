# Implicit actions when you define a function in the parent, 
# but not in the child
class Parent(object):
    
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
