func minSubArrayLen(target int, nums []int) int {
    sum:=0
    start:=0
    ans:= len(nums)+1
    for i:=0;i<len(nums);i++ {
        sum = sum + nums[i]
        // fmt.Println(sum, start, i, ans)
        for sum>=target {
            if ans > i - start + 1 {
                ans = i-start + 1
            }
            sum = sum - nums[start]
            start = start + 1
        }
    }
    return ans% (len(nums)+1)
    
}