class Twitter:

    def __init__(self):
        self.userList = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.userTweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        for followee in self.userList[userId]:
            ans.extend(self.userTweets[followee])
        ans.extend(self.userTweets[userId])
        ans.sort(key = lambda x:-x[0])
        res = [ans[i][1] for i in range(len(ans))]
        if len(res)<=10:
            return res
        return res[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userList[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userList:
            self.userList[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)