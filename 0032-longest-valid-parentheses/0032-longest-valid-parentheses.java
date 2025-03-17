class Solution {
    public int longestValidParentheses(String s) {
        int answer = 0;
        int len = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '('){
                stack.push(i);
            } else{
                if(stack.empty()){
                    continue;
                }
                stack.pop();
                if (stack.empty()){
                    stack.push(i);
                }
                else{
                    answer = (answer > i - stack.peek()) ? answer :  i - stack.peek();
                }
            }
        }
        return answer;
    }
}