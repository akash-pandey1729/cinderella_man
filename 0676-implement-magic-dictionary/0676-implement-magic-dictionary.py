class MagicDictionary:

    def __init__(self):
        self.dict1 = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict1 = set(dictionary)

    def search(self, searchWord: str) -> bool:
        def isDiffOne(word):
            for i in range(len(word)):
                t = word[i]
                for asci in range(97,97+26):
                    if asci!= ord(t):
                        temp = word[0:i] + chr(asci) + word[i+1:]
                        if temp in self.dict1:
                            return True
            return False
        return isDiffOne(searchWord)



        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)