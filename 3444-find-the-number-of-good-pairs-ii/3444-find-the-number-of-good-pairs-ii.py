class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num1_factor = defaultdict(int)
        def getFactor(num):
            factor = set()
            for i in range(1,int(math.sqrt(num))+1):
                if num%i==0:
                   factor.add(i)
                   factor.add(num//i)
            return factor
        
        for num in nums1:
            if num%k==0:
                d = getFactor(num//k)
                for element in d:
                    num1_factor[element]+=1
        ans = 0
        for num in nums2:
            ans+=num1_factor[num]
        return ans



        