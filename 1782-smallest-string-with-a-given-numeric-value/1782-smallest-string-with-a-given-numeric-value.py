# number+96  is done to get ascii value of lowercase character corresponding to the number
class Solution:
    def __init__(self):
        self.result = []

    def recursive_find(self, number, remaining):
        if remaining == 1: # Just one spot is remaining, use the character itself
            self.result.append(chr(number+96))
            return

        maximum_can_use = min(26, number - remaining + 1) # Find the biggest character you can use
        char = chr(maximum_can_use + 96)
        self.result.append(char)
        self.recursive_find(number-maximum_can_use, remaining-1)

    def getSmallestString(self, n: int, k: int) -> str:
        self.recursive_find(k, n)
        return ''.join(self.result[::-1])