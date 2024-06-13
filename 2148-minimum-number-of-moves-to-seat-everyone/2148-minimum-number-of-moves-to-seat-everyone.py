class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for i in range(len(students)):
            ans+=abs(students[i]-seats[i])
        return ans

        