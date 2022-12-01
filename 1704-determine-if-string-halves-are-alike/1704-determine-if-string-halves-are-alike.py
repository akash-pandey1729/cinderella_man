class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        s = s.lower()
        first = s[:len(s)//2]
        second = s[len(s)//2:]
        _first = 0
        _second = 0
        for i in range(len(first)):
            if first[i] in vowels:
                _first+=1
            if second[i] in vowels:
                _second+=1
        return _first==_second
        