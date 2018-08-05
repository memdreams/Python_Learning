class Other(object):
    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other's altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child's override()"

    def altered(self):
        print "Before Child's altered()"
        self.other.altered()
        print "After Child's altered()"


son = Child()

son.implicit()
son.override()
son.altered()
