func lengthOfLongestSubstring(s string) int {
    start:=-1
    ans:=0
    dict1:= make(map[byte]int)
    for i:=0;i<len(s);i++ {
        if _, ok:= dict1[s[i]]; ok {
            start = int(math.Max(float64(start), float64(dict1[s[i]])))
        }
        dict1[s[i]] = i
        ans = int(math.Max(float64(ans), float64(i-start)))  
    }
    return ans
    
}