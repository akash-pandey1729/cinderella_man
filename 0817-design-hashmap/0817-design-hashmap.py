class MyHashMap:

    def __init__(self):
        self.key_space = 1000
        self.dict1 = [[] for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        idx = key%self.key_space
        for i in range(len(self.dict1[idx])):
            if self.dict1[idx][i][0]==key:
                self.dict1[idx][i][1] = value
                return 
        self.dict1[idx].append([key, value])
        return 



    def get(self, key: int) -> int:
        idx = key%self.key_space
        for k,v in self.dict1[idx]:
            if k==key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        idx = key%self.key_space
        for i in range(len(self.dict1[idx])):
            if self.dict1[idx][i][0]==key:
                del self.dict1[idx][i]
                return 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)