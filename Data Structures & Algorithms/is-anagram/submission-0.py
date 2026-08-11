class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen=sorted(s)
        saw=sorted(t)
        if saw == seen:
            return True
        return False
