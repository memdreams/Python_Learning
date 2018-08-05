
wordsmapping = {
                    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
                    'verb': ['go', 'stop', 'kill', 'eat'],
                    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
                    'noun': ['door', 'bear', 'princess', 'cabinet']
                   }
types = ['direction', 'verb', 'stop', 'noun', 'number']

wordslist = []
for i in wordsmapping.values():
    wordslist += i

def scan(wordstr):
    words = wordstr.split()
    results = []
    for word in words:
        if word.isdigit():
            results.append(('number', int(word)))
        elif word.lower() in wordslist:
            word = word.lower()
            for key, values in wordsmapping.items():
                if word in values:
                    results.append((key, word))
        else:
            results.append(('error', word))
    return results


print(scan("HELLO in bear"))
