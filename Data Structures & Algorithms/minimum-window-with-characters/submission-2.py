class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        
        if len(s) < len(t):
            return ""
        
        for char in t:
            count[char] = 1 + count.get(char, 0)

        need = len(count)
        windowCount = {}
        have = 0
        l = 0
        minLen = float("inf")
        bestL = 0
        bestR = 0

        for r in range(len(s)):
            if s[r] in count:
                windowCount[s[r]] = 1 + windowCount.get(s[r], 0)
                if windowCount[s[r]] == count[s[r]]:
                    have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    bestL = l
                    bestR = r

                if s[l] in count:
                    windowCount[s[l]] -= 1
                    if windowCount[s[l]] < count[s[l]]:
                        have -= 1
                l += 1
        if minLen == float("inf"):
            return ""

        return s[bestL:bestR + 1]



