class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def helper(idx, res, target):
            if target == 0:
                ans.append(res[:])
                return
            for i in range(idx,len(candidates)):
                # crucial step!!!
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i]<0:
                    return
                helper(i+1,res + [candidates[i]], target - candidates[i])
        helper(0, [], target)
        return ans


        