class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let left = 0;
        let right  = 1;
        let result = 0
        

        while(right < prices.length){

            if(prices[left] < prices[right]){
                let profit = prices[right] - prices[left];
                result = Math.max(result, profit)
            }else{
                left = right
            }
            right++
        }

        return result
    }
}
