class Solution {
    private String s, p;
    public boolean isMatch(String s, String p) {
        int sLen = s.length();
        int pLen = p.length();

        boolean[][] dp = new boolean[sLen+1][pLen+1];
        dp[0][0] = true;

        for (int j = 2; j <= pLen; j++){
            if (p.charAt(j-1) == '*'){
                dp[0][j] = dp[0][j-2]; 
            }
        }

        for (int i = 1; i <= sLen; i++){
            for (int j = 1; j <= pLen; j++){
                char sc = s.charAt(i-1);
                char pc = p.charAt(j-1);
                if (sc == pc || pc == '.'){
                    dp[i][j] = dp[i-1][j-1];
                } else if (pc == '*') {
                    dp[i][j] = dp[i][j-2];

                    char pcPrev = p.charAt(j-2);
                    if (pcPrev == sc || pcPrev == '.'){
                        dp[i][j] |= dp[i-1][j];
                    }
                }

            }
        }
        return dp[sLen][pLen];
    }
}