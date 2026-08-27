class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        check = {}

        for num in nums:
            check[num] = 1 + check.get(num, 0)
        
        for key, val in check.items():
            bucket[val].append(key)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

       