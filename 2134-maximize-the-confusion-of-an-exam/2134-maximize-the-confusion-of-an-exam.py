class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = 0
        maxLen = 0
        countDict = {'T': 0, 'F': 0}

        for right in range(n):
            countDict[answerKey[right]] += 1

            # If the count of the opposite character is greater than k, move the left pointer
            while countDict['T'] > k and countDict['F'] > k:
                countDict[answerKey[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
