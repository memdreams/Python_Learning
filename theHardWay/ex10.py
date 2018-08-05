tabby_cat = "\tI'm tabbed \bin."
persian_cat = "I'm split\non a line. \b\\b usage.\b"
backslash_cat = "I'm %s a %r cat. " % ('\'', '\f')

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\v* 1 \v* 1.1 \v* 1.1.1\n\v* 2 \v* 2.1
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

f = True
# while f:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,
