# set whileLoop function with n loops
def whileLoop(n, step=1):
    i = 0
    numbers = []

    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print " Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

# numbers = whileLoop(6, 2)
# print "The numbers:"

numberLists = []
for i in range(6):
    print "At the top i is %d" % i
    numberLists.append(i)
    i += 1
    print " Numbers now: ", numberLists
    print "At the bottom i is %d" % i
