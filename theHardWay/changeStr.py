"""
Change variable names in ex5.py
"""

filename = 'ex5.py'

with open(filename) as r:
	data = r.readlines()
with open(filename, 'w') as f:
	for line in data:
		f.write(line.replace('my_', ''))



