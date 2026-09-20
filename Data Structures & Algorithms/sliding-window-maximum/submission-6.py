class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l = 0
        res = []

        for i , v in enumerate(nums):
            #Remove smaller element from deque
            while d and v >= d[-1][1]:
                d.pop()
            #Insert value in deque
            d.append((i, v))
            #Remove elemet that out side the window 
            if d and l > d[0][0]:
                d.popleft()
            #Check window size equal with k
            if (i - l + 1) == k:
                #insert the max value from the deque
                res.append(d[0][1])
                #window slide
                l += 1
        return res
            

