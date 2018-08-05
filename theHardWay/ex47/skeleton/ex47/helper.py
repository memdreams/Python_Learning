"""
Check duplicated code and delete it.
"""

def helper(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        print(data)

    with open(filename, 'w') as f:
        for line in data:
            # line = line.strip()
            if data.count(line) > 1 and line != ('\n' or '\t'):
                data.remove(line)
        for line in data:
            f.write(line)
    print(data)
    return data

# helper('game.py')
