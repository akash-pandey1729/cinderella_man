class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)==0:
            return s2==s3
        if len(s2)==0:
            return s1==s3
        if len(s3)==0:
            return False
        if len(s1) + len(s2)!=len(s3):
            return False
        # print(len(s3),len(s1),len(s2))
        def func(i,turn_s1,prev_s1,prev_s2):
            nonlocal s1
            nonlocal s2
            if i>len(s3)-1:
                print("idhar",i,turn_s1,prev_s1,prev_s2)
                if dp[turn_s1][prev_s1][prev_s2][i]=='-1':
                    flag = False
                    if prev_s1>=len(s1)-1 and prev_s2>=len(s2)-1:
                        dp[turn_s1][prev_s1][prev_s2][i]=  True
                        flag = True
                    if not flag:
                        dp[turn_s1][prev_s1][prev_s2][i] = False
                return dp[turn_s1][prev_s1][prev_s2][i]
            if turn_s1:
                if dp[turn_s1][prev_s1][prev_s2][i]=='-1':
                    flag = False
                    for j in range(i+1,len(s3)+1):
                        t = s1[prev_s1:].find(s3[i:j])
                        if t==0:
                            temp =  func(j,False,prev_s1+j-i,prev_s2)
                            if temp:
                                dp[turn_s1][prev_s1][prev_s2][i] = True
                                flag = True
                                break
                    if not flag:
                        dp[turn_s1][prev_s1][prev_s2][i] = False
                return dp[turn_s1][prev_s1][prev_s2][i]
            else:
                if dp[turn_s1][prev_s1][prev_s2][i]=='-1':
                    flag = False
                    for j in range(i+1,len(s3)+1):
                        t = s2[prev_s2:].find(s3[i:j])
                        if t==0:
                            temp =  func(j, True,prev_s1,prev_s2+j-i)
                            if temp:
                                dp[turn_s1][prev_s1][prev_s2][i] = True
                                flag = True
                                break
                    if not flag:
                        dp[turn_s1][prev_s1][prev_s2][i] = False         
                return dp[turn_s1][prev_s1][prev_s2][i]
        dp = [[[['-1' for i in range(len(s3)+1)] for i in range(len(s2)+1)]for i in range(len(s1)+1)]for i in range(2)]
        t1 = func(0,True,0,0) 
        # print("t1",t1)
        dp = [[[['-1' for i in range(len(s3)+1)] for i in range(len(s2)+1)]for i in range(len(s1)+1)]for i in range(2)]
        t2 = func(0,False,0,0)
        return t1 or t2
        
        