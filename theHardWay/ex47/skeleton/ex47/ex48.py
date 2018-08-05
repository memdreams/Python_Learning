
class Lexicon(object):
    wordsmapping = {
                    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
                    'verb': ['go', 'stop', 'kill', 'eat'],
                    'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
                    'noun': ['door', 'bear', 'princess', 'cabinet']
                   }
    types = ['direction', 'verb', 'stop', 'noun', 'number']

    def __init__(self):
        self.wordslist = []
        for i in Lexicon.wordsmapping.values():
            self.wordslist += i

    def scan(self, wordstr):
        words = wordstr.split()
        results = []
        for word in words:
            if word.isdigit():
                results.append(('number', int(word)))
            elif word.lower() in self.wordslist:
                word = word.lower()
                for key, values in Lexicon.wordsmapping.items():
                    if word in values:
                        results.append((key, word))
            else:
                results.append(('error', word))
        return results



lexicon = Lexicon()
print(lexicon.scan("HELLO in bear"))
