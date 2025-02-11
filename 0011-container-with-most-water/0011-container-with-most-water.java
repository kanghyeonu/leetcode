class Solution {
    public int maxArea(int[] height) {
        int r = height.length-1;
        int l = 0;
        int answer = 0;
        while (l < r) {
            int container = (r - l) * Math.min(height[r], height[l]);

            answer = Math.max(answer, container);

            if (height[r] < height[l]){
                r--;
            } else {
                l++;
            }
        }

        return answer;
    }
}