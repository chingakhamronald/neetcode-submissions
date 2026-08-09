class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        let countMap = new Map();

        for(let i = 0; i <= nums.length; i++){

            const completion = target - nums[i];

            if(countMap.has(completion)){
                return [i , countMap.get(completion)]
            }

            countMap.set(nums[i], i)
        }
    }
}
 