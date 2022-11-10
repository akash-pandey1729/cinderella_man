class Preferences:
    def __init__(self, userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests):
        self.userId = userId
        self.gender = gender
        self.preferredGender = preferredGender
        self.age = age
        self.minPreferredAge = minPreferredAge
        self.maxPreferredAge  = maxPreferredAge
        self.interests = interests
class Tinder:

    def __init__(self):
        self.user_list = {}

    def signup(self, userId: int, gender: int, preferredGender: int, age: int, minPreferredAge: int, maxPreferredAge: int, interests: List[str]) -> None:
        if userId not in self.user_list:
            self.user_list[userId] = Preferences(userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests)
        
    def getMatches(self, userId: int) -> List[int]:
        if userId in self.user_list:
            givenObj = self.user_list[userId]
            ans = []
            for key in self.user_list:
                if key!=userId:
                    if self.user_list[key].gender == givenObj.preferredGender and (givenObj.minPreferredAge<=self.user_list[key].age<=givenObj.maxPreferredAge):
                        temp = 0
                        for interest in givenObj.interests:
                            if interest in self.user_list[key].interests:
                                temp+=1
                        if temp>0:
                            ans.append([key, temp])
            ans.sort(key = lambda x:x[0])
            ans.sort(key = lambda x:-x[1])
            res = [ans[i][0] for i in range(len(ans))]
            if len(res)<=5:
                return res
            return res[:5]
                    
        


# Your Tinder object will be instantiated and called as such:
# obj = Tinder()
# obj.signup(userId,gender,preferredGender,age,minPreferredAge,maxPreferredAge,interests)
# param_2 = obj.getMatches(userId)