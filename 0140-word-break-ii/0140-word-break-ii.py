class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def getSentences(s, sentence):
            # print("s is ",s , "sentence is ",sentence)
            if s == "":
                ans.append(sentence[1:])
                return
            for i in range(len(s)+1):
                if s[0:i] in wordDict:
                    getSentences(s[i:], sentence + " " + s[0:i])
            return 
        getSentences(s, "")
        return ans







        