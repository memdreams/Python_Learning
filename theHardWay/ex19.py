# define a function named cheese_and_crackers which just print the input data
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


def add_something(x, y):
    print "x + y = %s" % (x+y)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

a, b = 1, 5
add_something(10, 20)
add_something('hi', 's')
add_something(a, b)
add_something(x=a, y=b)
add_something(10 + 10, 1 + 1)
add_something(['a', 'b'], [1, 2])
