class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1= {}
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] +1
        A = []
        for i in nums2:
            if i in dict1:
                A.append(i)
                dict1[i] = dict1[i] - 1
                if(dict1[i]==0):
                    del dict1[i]
        return A
            
        