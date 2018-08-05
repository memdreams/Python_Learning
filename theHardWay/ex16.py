from sys import argv # import argv method from sys library

script, filename = argv  # assign script and filename from input arguments

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-D (^D)." # in macOS; but CTRL-C in windows
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()  # since 'w' means rewirte the file, so we don't need to truncate it.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

f = open(filename)
lines = f.read()
print lines
f.close()
