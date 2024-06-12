class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        abbr = list(abbr)
        while i<len(word) and abbr:
            t = abbr.pop(0)
            if t=="0":
                return False
            while t.isdigit() and abbr and abbr[0].isdigit():
                t+= abbr.pop(0)
            if t.isdigit():
                i+= int(t)
            else:
                if t == word[i]:
                    i+=1
                else:
                    return False
        if abbr or i!=len(word):
            return False
        return True
        