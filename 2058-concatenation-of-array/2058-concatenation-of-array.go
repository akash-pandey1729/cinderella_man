import "fmt"
func getConcatenation(nums []int) []int {
    var ans []int
    for i:=0;i<2*len(nums);i++{
        ans = append(ans, nums[i%len(nums)])
    }
    return ans
}