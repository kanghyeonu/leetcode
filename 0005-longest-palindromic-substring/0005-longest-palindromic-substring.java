class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2 || new StringBuffer(s).reverse().toString().equals(s) ){
            return s;
        }

        int start = 0, end = 0;
        for (int i = 0; i < s.length()-1; i++){
            int[] result = checkPalindromic(i, i, s);
            if (end - start < result[1] - result[0]){
                start = result[0];
                end = result[1];
            }
            if (s.charAt(i) == s.charAt(i+1)){
                result = checkPalindromic(i, i+1, s);
                if (end - start < result[1] - result[0]){
                    start = result[0];
                    end = result[1];
                }
            }    
        }
        return s.substring(start, end + 1);
    }

    private int[] checkPalindromic(int l, int r, String s){
        int left = l, right = r;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            left -= 1;
            right += 1;
        }
        return new int[]{left+1, right-1};
    }   
}