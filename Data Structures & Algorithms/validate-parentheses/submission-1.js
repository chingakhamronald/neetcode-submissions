class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const bracket = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        const stack = [];

        for(let brac of s){
            if(bracket[brac]){
               const top = stack.pop()

               if(top !== bracket[brac]){
                return false
               }
            }else{
                stack.push(brac)
            }
            
        }

        return stack.length === 0 
    }
}
