class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            res = max(res, (r - l + 1))
            r += 1
        return res


        
       

            
        