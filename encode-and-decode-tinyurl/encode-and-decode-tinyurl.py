class Codec:
    def __init__(self):
        self.dict1 = defaultdict(int)
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id+=1
        self.dict1[self.id] = longUrl
        return self.id
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict1[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))