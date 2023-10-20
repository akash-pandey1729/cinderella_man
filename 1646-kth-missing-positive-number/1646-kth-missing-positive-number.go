func findKthPositive(arr []int, k int) int {
    set:= make(map[int]int)
    for i:=0;i<len(arr);i++{
        set[arr[i]] = 1
    }
    // fmt.Println(set)
    for i:=0;i<=2000;i++{
        if _,ok:= set[i]; ok{
            continue
        } else{
            if k==0{
                return i
            }
            k--
        }
    }
    return 1000
}