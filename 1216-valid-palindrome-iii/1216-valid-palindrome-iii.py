class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def lcs(X, Y):
            m = len(X)
            n = len(Y)
            L = [[0 for i in range(n+1)] for j in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif X[i-1] == Y[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])
            lcs = ""
            i = m
            j = n
            while i > 0 and j > 0:
                if X[i-1] == Y[j-1]:
                    lcs += X[i-1]
                    i -= 1
                    j -= 1
                elif L[i-1][j] > L[i][j-1]:
                    i -= 1

                else:
                    j -= 1
            lcs = lcs[::-1]
            return lcs
        # print(lcs(s,s[::-1]))
        if len(lcs(s,s[::-1]))>= len(s) - k:
            return True
        return False
        

        