class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        for key in cnt_t.keys():
            if key not in cnt_s or cnt_s[key]<cnt_t[key]:
                return key
        