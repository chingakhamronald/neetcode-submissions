class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let max = Math.max(...piles);

        for(let k = 1; k <= max; k++){
            let hour = 0;

            for(let num of piles){
                hour += Math.ceil(num / k);
            }

            if(hour <= h){
                return k
            }
        }
    }
}
