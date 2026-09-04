class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        res = [0] * n

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1] # pre[1] = 1 * 1
        for i in range(len(nums) - 2, -1 , -1):  # 4 - 2 = 2 
            suf[i] = nums[i + 1] * suf[i + 1] # suf[2] = nums[3] = 6 * 1
        for i in range(n):
            res[i] = pre[i] * suf[i]
        
        return res
        
       

        