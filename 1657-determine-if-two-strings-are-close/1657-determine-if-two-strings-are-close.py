class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        w1 = set(word1)
        w2 = set(word2)
        if w1!=w2:
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        s1 = [c1[key] for key in c1]
        s2 = [c2[key] for key in c2]
        s1.sort()
        s2.sort()
        return s1==s2
            
        