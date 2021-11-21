"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    ...
    def __init__(self,path,file = []):
        self.path = path
        count = 0
        self.file = open(f'{self.path}','r')
        for line in self.file:
            file.append(line)
            count += 1
        self.file = file
        print(f'{count} words read')
        # self.file.close()

    def random(self):
        return (random.choice(self.file))
        

# wf = WordFinder("words.txt")
# print(wf.random())