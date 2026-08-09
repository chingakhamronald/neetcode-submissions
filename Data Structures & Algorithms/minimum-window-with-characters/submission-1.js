class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
       if(t === "") return "";

       let need = new Map();

       for(let char of t){
        need.set(char, (need.get(char) || 0) + 1);
       }

       let required = need.size;
       let left = 0;
       let windowCount = new Map();
       let formed = 0;
       let res = [Infinity, null, null];

       for(let right = 0; right < s.length; right++){

        const c = s[right];
        windowCount.set(c, (windowCount.get(c) || 0) + 1);

        if(need.has(c) && windowCount.get(c) === need.get(c)){
            formed++
        }

        while(left <= right && required === formed){

            if((right - left + 1) < res[0]){
                res = [right - left + 1, left, right]
            }

            let leftChar = s[left];

            windowCount.set(leftChar, windowCount.get(leftChar) - 1);

            if(need.has(leftChar) && windowCount.get(leftChar) < need.get(leftChar)){
                formed--
            }
            left ++
        }
       }
    return res[0] === Infinity ? "" : s.slice(res[1], res[2] +1)
    }
}
