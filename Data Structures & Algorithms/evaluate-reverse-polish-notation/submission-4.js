class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];

        for(let num of tokens){
            if(num === '+'){
               stack.push(stack.pop() + stack.pop())
            } else if(num === '-'){
                 let a = stack.pop() 
                 let b = stack.pop()
                 stack.push(b - a)
            } else if(num === '*'){
                 stack.push(stack.pop() * stack.pop())
            } else if(num === '/'){
                let a = stack.pop() 
                 let b = stack.pop()
                 stack.push(Math.trunc(b / a))
            }else{
                stack.push(Number(num))
            }
        }

        return stack.pop()
    }
}
