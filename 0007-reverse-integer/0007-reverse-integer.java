class Solution {
    public int reverse(int x) {
        boolean isMinus = (x < 0) ? true : false;
        int abs_x = Math.abs(x);

        String str_x = String.valueOf(abs_x);
        StringBuilder sb= new StringBuilder(str_x);
        sb.reverse();
        
        int answer;
        try{
            answer = Integer.parseInt(sb.toString());
        } catch(NumberFormatException e){
            answer = 0;
        }
        

        return (isMinus) ? answer*-1 : answer;
        
    }
}