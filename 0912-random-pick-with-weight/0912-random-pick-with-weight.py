class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        self.tots = sum(w)
        self.mapping = []
        last_idx = 0
        for i in range(len(w)):
            self.mapping.append((last_idx, i))
            last_idx = last_idx+w[i]
        
    def pickIndex(self) -> int:
        idx = random.randint(0, self.tots-1)
        j = (bisect.bisect_right(self.mapping, (idx,)))
        return self.mapping[j-1][1]
