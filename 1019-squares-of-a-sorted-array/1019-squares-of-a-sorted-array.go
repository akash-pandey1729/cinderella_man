
func sortedSquares(nums []int) []int {
    for i:=0;i<len(nums);i++{
        nums[i] = nums[i]*nums[i]
    }
    sort.Ints(nums)
    return nums
}