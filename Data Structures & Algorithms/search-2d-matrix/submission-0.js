
class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target , store = []) {
      
      for(let i = 0; i < matrix.length; i++){
        if(Array.isArray(matrix[i])){
          this.searchMatrix(matrix[i], target, store)
        }else{
          store.push(matrix[i])
        }
      }
      
      let l = 0;
      let r = store.length - 1;
      
      while(l <= r){
        
        const m = Math.floor((l + r) / 2);
        
        if(store[m] === target){
          return true
        }else if(store[m] > target){
          r = m - 1;
        }else {
          l = m + 1;
        }
        
        
        
      }
      
      return false;
    }
}
