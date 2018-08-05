# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10  # given a int type value
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x  # %r means repr()
print "I also said: '%s'." % y  # '%s' looks like %r

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e  # concascate w and e
