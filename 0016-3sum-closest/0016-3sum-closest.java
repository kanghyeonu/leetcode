class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int answer = 0;
        int minGap = Integer.MAX_VALUE;
        
        for (int i = 0; i < nums.length; i++){
            int n = nums[i];
            if (i >= 1 && nums[i] == nums[i-1]){
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;
            while (left < right){
                int sum = n + nums[left] + nums[right];           
                int gap = Math.abs(target - sum);
                if (minGap > gap){
                    answer = sum;
                    minGap = gap;
                }
                if ( target < sum ){               
                    while (left < right && nums[right] == nums[right-1]){
                        right--;
                    }
                    right--;               
                } else if (sum < target) {
                    while(left < right && nums[left] == nums[left+1]){
                        left++;
                    }
                    left++;
                } else{
                    return sum;
                }
            }
        }
        return answer;
    }
}