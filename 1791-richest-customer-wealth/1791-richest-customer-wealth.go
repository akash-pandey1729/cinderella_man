func maximumWealth(accounts [][]int) int {
    var sum int
    for i:=0;i<len(accounts);i++{
        var temp int
        for j:=0;j<len(accounts[0]);j++{
            temp+= accounts[i][j]
        }
        if sum <temp{
            sum = temp
        }
    }
    return sum
}