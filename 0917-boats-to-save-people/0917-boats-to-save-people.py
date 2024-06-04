class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = 0
        while people:
            n+=1
            if len(people)>1 and people[0]+people[-1]<=limit:
                people.pop(0)
                people.pop()
            else:
                people.pop()
        return n


        


        