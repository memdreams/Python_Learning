people = int(raw_input())
cars = 40
buses = 15

# judge the condition based on the values of cars and people and enter in relevant branch
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We shouldn't take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
