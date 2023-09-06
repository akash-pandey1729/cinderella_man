class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        start = newInterval[0]
        end = newInterval[1]
        for interval in intervals:
            if interval[0]<=newInterval[0] <= interval[1]:
                start = interval[0]
            if interval[0]<=newInterval[1] <= interval[1]:
                end = interval[1]
            elif start<=interval[0] and end >= interval[1]:
                continue
            else:
                ans.append(interval)
        ans.append([start, end])
        ans.sort(key = lambda x:x[0])
        return ans
            

        
        