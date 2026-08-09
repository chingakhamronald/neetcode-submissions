class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = new Map();

        for(let str of strs){

            const countStr = Array(26).fill(0);
            for(let char of str){
                countStr[char.charCodeAt(0) - "a".charCodeAt(0)]++
            }
            const key = countStr.join("#");

            if(!map.has(key)){
                map.set(key, [])
            }

            map.get(key).push(str)
        }

        return [...map.values()]
    }
}
