class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}:{word}"
        return encoded_str
    
    def decode(self, encoded_str: str) -> list[str]:
        decoded = []
        i = 0
        while i < len(encoded_str):
            length = int(encoded_str[i])
            decoded.append(encoded_str[i+2:i+2+length])
            i += 2 + length
        return decoded
    

if __name__ == "__main__":
    words = ["lint", "code", "love", "you"]
    sol = Solution()
    encoded = sol.encode(words)
    decoded = sol.decode(encoded)
    assert decoded == words
    print(words)
    print("Encoded =", encoded)
    print("Decoded =", decoded)