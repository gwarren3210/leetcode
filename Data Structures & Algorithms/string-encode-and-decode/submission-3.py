class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return "ד"
        return 'ש'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "": return [""]
        if s == "ד": return []
        return s.split('ש')