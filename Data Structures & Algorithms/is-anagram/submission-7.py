class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = 1 + seen.get(char, 0)
        for char in t:
            if char not in seen:
                return False
            seen[char] =  seen.get(char) - 1
            if seen.get(char) == 0:
                del seen[char]
        return len(seen) == 0