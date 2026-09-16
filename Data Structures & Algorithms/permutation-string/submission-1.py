class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        s1Count = {}
        windowCount = {}

        for char in s1:
            s1Count[char] = 1 + s1Count.get(char, 0)

        l = 0
        for r in range(len(s2)):
            windowCount[s2[r]] = 1 + windowCount.get(s2[r], 0)

            if (r - l + 1) > len(s1):
                windowCount[s2[l]] -= 1
                if windowCount[s2[l]] == 0:
                    del windowCount[s2[l]]
                l += 1 
            
            if windowCount == s1Count:
                return True
        return False
        


       