## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Cat is-a Animal, also is-a object
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a __init__ that takes self, name parameters
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a __init__ that takes self, name parameters
        self.name = name

## Person is-a Object
class Person(object):

    def __init__(self, name):
        ## Person has-a __init__
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person, also is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a __init__, also inherit from Person's __init__
        super(Employee, self).__init__(name)
        ## __init__ has-a salary attribute
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat, is an instance
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet is-a instance of Cat
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", "120000")

## frank has-a pet is-a Dog
frank.pet = rover

## flipper is-a Fish
filipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
