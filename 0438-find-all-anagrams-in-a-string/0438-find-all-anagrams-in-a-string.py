class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        temp = ''.join(sorted([i for i in p]))
        ans = []
        for i in range(0,len(s)-len(p)+1):
            if ''.join(sorted(s[i:i+len(p)])) == temp:
                ans.append(i)
        return ans

        