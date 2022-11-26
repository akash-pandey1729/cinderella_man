class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        _left = [1]*n
        
        stack = [0]
        for i in range(1, n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            _left[i] = i - stack[-1] if stack else i+1
            stack.append(i)
        # print(stack)
        # print(_left)
        # print()
        
        _right = [1]*n
        stack = [n-1]
        for i in range(n-2,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            _right[i] = stack[-1] - i if stack else n -i
            stack.append(i)
        # print(stack)
        # print(_right)
        ans = 0
        for i in range(n):
            ans += _right[i]*_left[i]*arr[i]
        return ans%(10**9+7)
            
                
        