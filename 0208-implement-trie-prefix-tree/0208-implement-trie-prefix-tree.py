from collections import defaultdict
class Trie:
    def __init__(self):
        self.root_dict = defaultdict(dict)
        
    def insert(self, word: str) -> None:
        def help(word, dict1):
            if not word:
                dict1['end'] = True
                return
            if word[0] not in dict1:
                dict1[word[0]] = {"end": False}
            help(word[1:], dict1[word[0]])
        help(word, self.root_dict)
        # print(self.root_dict)
        
    def search(self, word: str) -> bool:
        def help(word, dict1):
            if not word and dict1['end']:
                return True
            if not word or word[0] not in dict1:
                return False
            return help(word[1:], dict1[word[0]])
        return help(word, self.root_dict)
        

    def startsWith(self, prefix: str) -> bool:
        def help(word, dict1):
            if not word:
                return True
            if not word or word[0] not in dict1:
                return False
            return help(word[1:], dict1[word[0]])
        return help(prefix, self.root_dict) 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)