class Solution:

    def encode(self, strs: List[str]) -> str:
        result: str = ""
        for s in strs:
            result += "<|start|>" + s + "<|end|>"
        return result

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        endTokenLen = len("<|end|>")
        for c in s.split("<|start|>"):
            if c != "":
                result.append(c[:len(c) - endTokenLen])
        return result