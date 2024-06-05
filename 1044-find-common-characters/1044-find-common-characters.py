class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_dict_list = [Counter(word) for word in words]
        ans = [float(inf)]*26
        print(len(ans))
        for i in range(0,26):
            present = True
            for word_dict in words_dict_list:
                if chr(i+97) not in word_dict:
                    present = False
                    break
                else:
                    ans[i] = min(ans[i], word_dict[chr(i+97)])
            if not present:
                ans[i] = float(inf)
        # print(ans)
        res= []
        for i in range(26):
            if ans[i]!=float('inf'):
                for _ in range(ans[i]):
                    res.append(chr(i+97))
        return res
        return [chr(i+97)*word_dict[chr(i+97)] for i in range(26) if ans[i]!=float('inf')]

        