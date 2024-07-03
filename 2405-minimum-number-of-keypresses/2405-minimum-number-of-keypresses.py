class Solution:
    def minimumKeypresses(self, s: str) -> int:
        s_dict = Counter(s)
        ch_order = [(s_dict[key], key) for key in s_dict]
        ch_order.sort()
        ch_order.reverse()
        # print(ch_order)
        # print()
        key_pad = defaultdict(list)
        heap = [(0,i) for i in range(1,10)]
        heapq.heapify(heap)
        for ch in ch_order:
            cnt, key = heapq.heappop(heap)
            if cnt<3:
                key_pad[key].append(ch[1])
                heapq.heappush(heap, (cnt+1, key))

        press_dict = defaultdict(int)
        for ch in ch_order:
            for key in key_pad:
                if ch[1] in key_pad[key]:
                    press_dict[ch[1]] = key_pad[key].index(ch[1])+1
        ans = 0
        # print(key_pad)
        # print()
        # print(s_dict)
        for ch in s:
            ans+= press_dict[ch]
        return ans
            







        


        