class Trie:

    def __init__(self):
        self.dict1 = {}
        
    def insert(self, word: str) -> None:
        def helper(word, dict1):
            if len(word)==1:
                if word[0] not in dict1:
                    dict1[word[0]] = {'Count': 1, 'isWord': 1}
                    return dict1
                else:
                    dict1[word[0]]['Count']+=1
                    dict1[word[0]]['isWord']+=1
                    return dict1
            elif word[0] not in dict1:
                dict1[word[0]] = {'Count': 1, 'isWord': 0}
                dict1[word[0]] =  helper(word[1:], dict1[word[0]])
                return dict1
            else:
                dict1[word[0]]['Count']+=1
                dict1[word[0]] =  helper(word[1:],dict1[word[0]])
                return dict1
        self.dict1 = helper(word, self.dict1)
        # print(self.dict1)
        # print()

    def countWordsEqualTo(self, word: str) -> int:
        def helper(word=word, dict1 = self.dict1):
            if len(word)==1:
                if word[0] not in dict1:
                    return 0
                return dict1[word[0]]['isWord']
            else:
                if word[0] not in dict1:
                    return 0
                return helper(word[1:],dict1[word[0]])
        return helper()
        

    def countWordsStartingWith(self, prefix: str) -> int:
        def helper(word=prefix, dict1 = self.dict1):
            if len(word)==1:
                if word[0] not in dict1:
                    return 0
                return dict1[word[0]]['Count']
            else:
                if word[0] not in dict1:
                    return 0
                return helper(word[1:],dict1[word[0]])
        return helper()
        

    def erase(self, word: str) -> None:
        def helper(word=word, dict1 = self.dict1):
            if len(word)==1:
                dict1[word[0]]['Count']-=1
                dict1[word[0]]['isWord']-=1
                if dict1[word[0]]['Count'] ==0:
                    del dict1[word[0]]
                return dict1
            else:
                dict1[word[0]]['Count']-=1
                if dict1[word[0]]['Count']==0:
                    del dict1[word[0]]
                else:
                    dict1[word[0]] =  helper(word[1:],dict1[word[0]])
                return dict1
        self.dict1 = helper()
        # print("delete ", self.dict1)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)