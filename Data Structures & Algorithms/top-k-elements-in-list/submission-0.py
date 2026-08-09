class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # count the frequency num
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # check frequency num
        for key, val in count.items():
            freq[val].append(key)

        res = []

        #iterate the top k numbers
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
