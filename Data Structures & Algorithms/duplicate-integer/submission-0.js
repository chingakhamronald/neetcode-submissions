class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let seen = new Map();

        for(let char of nums){
            seen.set(char, (seen.get(char) || 0) + 1);
            if(seen.get(char) > 1) return true;
        }
        
      return false
    }
}
