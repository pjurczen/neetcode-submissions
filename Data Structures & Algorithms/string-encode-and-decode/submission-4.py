class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}|{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        lenStr: str = ""
        i: int = 0
        while i < len(s):
            while s[i] != "|":
                lenStr += s[i]
                i += 1
            i += 1
            length = int(lenStr)
            result.append(s[i:i+length])
            lenStr = ""
            i += length
            
        return result