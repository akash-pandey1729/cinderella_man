class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first=edges[0][0]
        second=edges[0][1]
        if edges[1][0]==first or edges[1][1]==first:
            return first
        return second
    #please upvote me it would encourage me alot
