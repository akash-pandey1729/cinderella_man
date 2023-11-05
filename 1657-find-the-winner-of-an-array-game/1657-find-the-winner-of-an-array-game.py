class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)
        stack = []
        max_so_far = arr[0]
        # print(arr)
        for i in range(1,len(arr)):
            max_so_far = max(max_so_far,arr[i])
            if max_so_far>arr[i]:
                stack.append(arr[i])
            else:
                stack = [arr[i]]
            
            if len(stack)==k or i==len(arr)-1:
                    return max_so_far






            

        
        