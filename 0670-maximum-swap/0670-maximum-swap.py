class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = list(str(num))
        num_list = list(str(num))
        num_list.sort(reverse = True)
        print(num_list)
        dict1 = defaultdict(list)
        for i in range(len(temp)):
            dict1[temp[i]].append(i)
        for i in range(len(temp)):
            if temp[i]==num_list[i]:
                continue
            else:
                idx_1 = dict1[num_list[i]][-1]
                temp[idx_1], temp[i] = temp[i], temp[idx_1]
                return int("".join(temp))
        return num



        