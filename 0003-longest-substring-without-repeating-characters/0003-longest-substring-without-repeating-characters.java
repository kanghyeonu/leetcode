class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        String longest = "";
        for (int i = 0; i < s.length(); i++){
            String ch = s.substring(i, i+1);
            if (longest.contains(ch)){
                int pos = longest.indexOf(ch);
                longest = longest.substring(pos+1) + ch;
            }
            else {
                longest += ch;
            }

            if (answer < longest.length()){
                answer = longest.length();
            }
        }

        return answer;
    }
}