class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }

        String xStr = Integer.toString(x);
        StringBuilder sb = new StringBuilder(xStr);
        sb.reverse();

        if (xStr.equals(sb.toString())){
            return true;
        } else{
            return false;
        }
    }
}