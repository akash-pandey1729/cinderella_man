class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors)<=2:
            return False
        def getmoves(l1, l2):
            moves = 0
            prev = colors[0]
            conseq = int(colors[0]==l1)
            for i in range(1, len(colors)):
                if prev == l1 and colors[i]==l1:
                    conseq+=1
                elif prev == l2 and colors[i]==l1:
                    prev = l1
                    conseq = 1
                elif colors[i]==l2:
                    prev = l2
                    if conseq>=3:
                        moves+= (conseq - 2)
                    conseq = 0
            if conseq>=3:
                    moves+= (conseq - 2)
            return moves
        moves_A = getmoves('A', 'B')
        moves_B = getmoves('B', 'A')
        return moves_A>moves_B



        