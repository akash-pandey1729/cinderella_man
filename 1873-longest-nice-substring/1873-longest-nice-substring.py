class Solution:
    def get_nice(self, s: str) -> bool:
        return len(set(s.lower())) == (len(set(s)) // 2)
        
    def longestNiceSubstring(self, s: str) -> str:
        window_size = len(s)
        
        while window_size:
            for i in range(len(s) - window_size + 1):
                substring = s[i:i + window_size]
                
                if self.get_nice(substring):
                    return substring
                
            window_size -= 1
            
        return ''