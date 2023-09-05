# class Node:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right
        
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.dict1 = {}
#         self.capacity = capacity
#         self.start = Node()
#         self.end = Node()
        
#     def get(self, key: int) -> int:
#         if key not in self.dict1:
#             return -1
#         return self.dict1[key].val
        
#     def put(self, key: int, value: int) -> None:
#         if not self.start:
#             self.start = Node(value, None, None)
#             self.dict1[key] = self.start
#             self.capacity-=1
#             self.end = self.start
#         else:
#             if key in self.dict1:
#                 temp = self.dict1[key]
#                 temp_left = self.dict1[key].left
#                 temp_right = self.dict1[key].left
#                 temp_left.right = temp_right
#                 temp_right.left = temp_left
#                 self.start.left = temp
#                 temp.right = self.start
#                 temp.left = None
#                 self.start = temp 
#             else:
#                 if self.capacity !=0:
#                     self.capacity-=1


        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key) 
            self.cache[key] = val
            return self.cache.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if len(self.cache.keys()) == self.capacity:
                del self.cache[next(iter(self.cache))]
        else:
            self.cache.pop(key)
        self.cache[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)