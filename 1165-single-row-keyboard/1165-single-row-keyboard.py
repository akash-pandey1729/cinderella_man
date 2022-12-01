class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        t = 0
        currIdx = 0
        dict1 = defaultdict()
        for idx, w in enumerate(keyboard):
            dict1[w] = idx
        for w in word:
            t+= abs(currIdx-dict1[w])
            currIdx = dict1[w]
        return t
            
        