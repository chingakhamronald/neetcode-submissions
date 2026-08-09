class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let temp = temperatures
        const res = new Array(temp.length).fill(0);
        const stack = []; // [temp, index];

        for(let i = 0; i < temp.length; i++){
            while(stack.length > 0 && temp[i] > stack[stack.length - 1][0]){
                const [stackT, stackInd] = stack.pop();
                res[stackInd] = i - stackInd;
            }
            stack.push([temp[i], i])
        }
        return res
    }
}
