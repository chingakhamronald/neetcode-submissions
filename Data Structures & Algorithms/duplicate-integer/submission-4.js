class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let numsMap = new Map();

        for(let char of nums){
            if(numsMap.has(char)){
                return true
            }
            numsMap.set(char)
        }

        return false
    }
}
