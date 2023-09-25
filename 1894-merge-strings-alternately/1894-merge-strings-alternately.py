class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        first = True
        i,j = 0,0
        while i<len(word1) and j<len(word2):
            if first:
                word+=word1[i]
                i+=1
                first = False
            else:
                word+=word2[j]
                j+=1
                first = True
        word+= word1[i:]
        word+=word2[j:]
        return word

        