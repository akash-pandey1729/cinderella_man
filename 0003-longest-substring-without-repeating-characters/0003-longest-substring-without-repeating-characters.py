class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longestSubstring = 0, 0
        windowChars = set()

        for r in range(len(s)):

            # close window
            if s[r] in windowChars:
                while s[r] in windowChars:
                    windowChars.remove(s[l])
                    l += 1
            # expand window
            windowChars.add(s[r])
            longestSubstring = max(longestSubstring, (r - l + 1))
        
        return longestSubstring

        