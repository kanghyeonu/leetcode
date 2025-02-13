class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minLen = 999999;
        for (int i = 0; i < strs.length; i++){
            minLen = (strs[i].length() <  minLen) ? strs[i].length() : minLen;
        }
        for (int i = 0; i < minLen; i++){
            for (int j = 1; j < strs.length; j++){
                if (strs[j].charAt(i) != strs[j-1].charAt(i)){
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0].substring(0, minLen);
    }
}