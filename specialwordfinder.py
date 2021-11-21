import random
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    '''SpecialWordFinder inherits from WordFinder with modified random method'''
    def __init__(self, path, file = []):
        super().__init__(path,file)

    def random(self):
        """modified random method disallows random choice to be '#' or blank line"""
        cleanfile = []
        for i in range(len(self.file)):
            if self.file[i].find('#') != 0 and self.file[i] != '\n':
                cleanfile.append(self.file[i])

        return random.choice(cleanfile)

        

        

wf1 = SpecialWordFinder('test.txt')
print(wf1.random())
