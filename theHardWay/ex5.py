# More Variables and Printing
name = 'Zed A. Shaw'
age = 35
height = 74  #inches
height_centi = height * 2.54  # inches to centimeters
weight = 180  #lbs
weight_kilo = weight * 0.453592  # pounds to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall, that is, %d centimeters tall." % (height, height_centi)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
