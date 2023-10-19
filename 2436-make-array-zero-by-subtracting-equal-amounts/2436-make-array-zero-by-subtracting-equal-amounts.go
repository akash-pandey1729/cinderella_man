func minimumOperations(nums []int) int {
    m := make(map[int]int)
    for i:=0;i<len(nums);i++{
        if nums[i]>0{
            if _, ok := m[nums[i]]; ok {
                m[nums[i]]++ 
            } else {
                m[nums[i]] = 1
            }
            
        }
    }
    var keys []int
    for k:=range(m){
        keys = append(keys,k)
    }
    return len(keys)

}