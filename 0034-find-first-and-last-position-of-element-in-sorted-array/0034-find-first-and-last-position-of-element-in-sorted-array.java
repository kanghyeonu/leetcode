class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start = -1;
        int end = -1;
        int index = Arrays.binarySearch(nums, target);
        if(index < 0){
            return new int[]{start, end};
        }
 
        for (int i = index; i >= 0; i--){
            if (nums[i] == target){
                start = i;
            }else{
                break;
            }
        }  

        for (int i = index; i < nums.length; i++){
            if (nums[i] == target){
                end = i;
            }else{
                break;
            }
        }
        
        return new int[]{start, end};
    }
}