class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        new_s = ""
        for ch in order:
            new_s+= ch*counter[ch]
            del counter[ch]
        for key in counter:
            new_s+=key*counter[key]
        return new_s



        