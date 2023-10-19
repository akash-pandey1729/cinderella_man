import ("fmt"; "bytes")

func getFinalString(s string) []byte {
        var slice []byte
        for i:=0; i<len(s);i++{
            if len(slice)>0 && s[i]== '#'{
                slice = slice[:len(slice)-1]
            }
            if s[i]=='#' {
                continue
            } else {
                slice = append(slice, byte(s[i]))
            }
        }
        return slice
    }
func backspaceCompare(s string, t string) bool {
    // fmt.Println(getFinalString(s))
    return bytes.Equal(getFinalString(s), getFinalString(t))
    
}