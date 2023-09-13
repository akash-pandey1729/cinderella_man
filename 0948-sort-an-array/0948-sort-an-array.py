class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = [[num] for num in nums]
        def mergeSort(nums):
            while len(nums)>1:
                new = []
                for i in range(0,len(nums),2):
                    if i==len(nums)-1:
                        new.append(nums[i])
                        continue
                    new.append(merge(nums[i], nums[i+1]))
                nums = new
            return nums[0]

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
            
        
        