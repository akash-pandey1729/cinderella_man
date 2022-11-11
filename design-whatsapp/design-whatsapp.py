class WhatsApp:

    def __init__(self):
        self.groups = defaultdict(set)
        self.users = defaultdict(set)
        self.userMessages = defaultdict(list)
        self.groupMessages = defaultdict(list)
        self.messageId = 0
        self.groupId = 0
        

    def sendMessage(self, toUser: int, message: str) -> None:
        self.messageId+=1
        self.userMessages[toUser].append([self.messageId, message])
            
    def createGroup(self, initialUsers: List[int]) -> int:
        self.groupId+=1
        self.groups[self.groupId].update(initialUsers)
        return self.groupId
        
    def addUserToGroup(self, groupId: int, userId: int) -> None:
        if groupId in self.groups:
            self.groups[groupId].add(userId)
        
    def sendGroupMessage(self, fromUser: int, groupId: int, message: str) -> None:
        if groupId in self.groups and fromUser in self.groups[groupId]:
            self.messageId+=1
            self.groupMessages[groupId].append(message)
            for user in self.groups[groupId]:
                if user!=fromUser:
                    self.userMessages[user].append([ self.messageId, message])
        
    def getMessagesForUser(self, userId: int) -> List[str]:
        res = self.userMessages[userId]
        res.sort(key = lambda x:-x[0])
        ans = [res[i][1] for i in range(len(res))]
        return ans
        


# Your WhatsApp object will be instantiated and called as such:
# obj = WhatsApp()
# obj.sendMessage(toUser,message)
# param_2 = obj.createGroup(initialUsers)
# obj.addUserToGroup(groupId,userId)
# obj.sendGroupMessage(fromUser,groupId,message)
# param_5 = obj.getMessagesForUser(userId)