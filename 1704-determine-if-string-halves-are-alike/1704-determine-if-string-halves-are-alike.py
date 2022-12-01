class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        first = s[:len(s)//2]
        second = s[len(s)//2:]
        _first = 0
        _second = 0
        for i in range(len(first)):
            if first[i] in vowels or first[i].lower() in vowels:
                _first+=1
            if second[i] in vowels or second[i].lower() in vowels:
                _second+=1
        return _first==_second
        