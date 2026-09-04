class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        
        for v, key in seen.items():
            bucket[key].append(v)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
       

       