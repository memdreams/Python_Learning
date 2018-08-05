from sys import argv # import argv method from sys library

script, filename = argv  # assign script and filename from input arguments

txt = open(filename)  # open the file with filename and save the file as txt

print "Here is your file %r:" % filename
print txt.read()  # print the content of the file.
txt.close()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
