class Solution {
    private List<String> answer = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        backtracking(n, n, "");
        return answer;
    }

    void backtracking(int open, int close, String s){
        if (open == 0 && close == 0){
            answer.add(s);
            return;
        }

        if (open > 0){
            backtracking(open-1, close, s + "(");
        } 
        if (close > open){
            backtracking(open, close-1, s + ")");
        }
    }
}