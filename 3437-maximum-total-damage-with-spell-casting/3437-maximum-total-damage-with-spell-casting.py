class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        @cache
        def helper(i = len(power)-1):
            if i < 0:
                return 0
            left = bisect.bisect_left(power, power[i])
            right = bisect.bisect_right(power, power[i])
            curr_sum = (right - left)*power[i]
            excluding = 0
            if left > 0 and power[left - 1] in [power[i] - 1, power[i] - 2]:
                excluding =  helper(left - 1)
            including_idx = bisect_right(power, power[i] - 3)
            return max(curr_sum+ helper(including_idx - 1), excluding)
        return helper()




        