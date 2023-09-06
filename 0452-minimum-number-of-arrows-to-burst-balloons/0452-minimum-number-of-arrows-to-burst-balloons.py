class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        stack = [points[0]]
        for idx in range(1, len(points)):
            if stack[-1][0]<=points[idx][0]<=stack[-1][1]:
                stack[-1][1] = min(points[idx][1], stack[-1][1])
            else:
                stack.append(points[idx])
        print(stack)
        return len(stack)
        