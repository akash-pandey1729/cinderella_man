class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums)==0:
                return []
            if len(nums)==1:
                return nums
            else:
                pivot = len(nums)//2
                left = mergeSort(nums[0:pivot])
                right = mergeSort(nums[pivot:])
                return merge(left,right)
        def merge(list1,list2):
            l = []
            while(len(list1)>0 and len(list2)>0):
                if list1[0]<=list2[0]:
                    l.append(list1.pop(0))
                else:
                    l.append(list2.pop(0))
            l.extend(list1)
            l.extend(list2)
            return l
        return mergeSort(nums)
            
        
        