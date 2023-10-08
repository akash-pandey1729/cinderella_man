class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse = True)
        task_max = []
        for i in range(3,len(tasks),4):
            task_max.append(tasks[i])
        # print(task_max)
        ans = 0
        for i in range(len(processorTime)):
            ans = max(ans,processorTime[i] + task_max[i] )
        return ans
        
        
        