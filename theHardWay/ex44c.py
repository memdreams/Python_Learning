class Parent(object):

    def altered(self):
        print "Parent's altered()"

class Child(Parent):

    def altered(self):
        print "Before Child's altered()"
        super(Child, self).altered()
        print "After Child's altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
