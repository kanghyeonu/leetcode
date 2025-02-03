class Solution {
    public int myAtoi(String s) {
        String stripStr = s.strip();
        if (stripStr.equals("")) {
            return 0;
        }

        boolean isMinus = false;
        int index = 0;

        // 부호 확인
        if (stripStr.charAt(0) == '-') {
            isMinus = true;
            index++;
        } else if (stripStr.charAt(0) == '+') {
            index++;
        }

        long answer = 0;

        // 숫자 처리
        while (index < stripStr.length()) {
            char c = stripStr.charAt(index);
            if (c < '0' || c > '9') {
                break; // 숫자가 아니면 중단
            }
            answer = answer * 10 + (c - '0'); // 숫자 추가

            // 범위 체크
            if (isMinus && -answer < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            } else if (!isMinus && answer > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }

            index++;
        }

        return isMinus ? (int) -answer : (int) answer;
    }
}