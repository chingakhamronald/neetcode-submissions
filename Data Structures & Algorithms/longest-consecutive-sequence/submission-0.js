class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {

        let store = new Set(nums);
        let longest = 0;

        for(let num of nums){

            if(!store.has(num - 1)){
                let length = 1;

                while(store.has(num + length)){
                    length ++
                }
                longest = Math.max(longest, length)
            }
        }

        return longest
    }
}
