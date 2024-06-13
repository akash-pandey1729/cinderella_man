class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        depths = defaultdict(int)
        ans = 0
        while paths:
            with_prefix = paths.pop(0)
            without_prefix = with_prefix[:].replace("\t", "")
            depth = len(with_prefix) - len(without_prefix)
            # if depth not in depths:
            depths[depth] = depths[depth-1] + len(without_prefix)
            # else:
            #     depths[depth] = depths[depth-1] + max( depths[depth]-depths[depth-1] ,len(without_prefix) )
            # print(depth, without_prefix)
            if "." in without_prefix:
                ans = max(ans, depths[depth]+ depth)
        print(depths)
        return ans

        