class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = Counter(ages)
        req = 0
        for key1 in cnt:
            for key2 in cnt:
                if key1!=key2 and key1>key2 and key2> 0.5 * key1 + 7:
                    print(key1, key2)
                    req+= cnt[key1]*cnt[key2]
        for key in cnt:
            if cnt[key]>1 and key>14:
                req+= cnt[key]*(cnt[key]-1)
        return req

        