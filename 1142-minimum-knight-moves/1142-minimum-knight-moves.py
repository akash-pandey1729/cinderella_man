class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        stack = [(0,0)]
        steps = -1
        visited = set()
        visited.add((0,0))
        while True:
            n = len(stack)
            steps+=1
            for i in range(n):
                p,q = stack.pop(0)
                if p==x and q==y:
                    return steps
                for a,b in [(p-2,q+1),(p-2,q-1),(p-1,q+2),(p-1,q-2),(p+1,q+2),(p+1,q-2),(p+2,q+1),(p+2,q-1)]:
                    if -300<=a<=300 and -300<=b<=300 and abs(a) + abs(b)<=300 and (a,b) not in visited:
                        # print(a,b)
                        visited.add((a,b))
                        stack.append((a,b))
        


        