class Solution {
    public int removeDuplicates(int[] nums) {
        int s = 0;
        for (int i= 1; i < nums.length; i++){
            if (nums[i] == nums[s]){
                continue;
            } 
            nums[s+1] = nums[i];
            s++;
            
        }
        return s+1;
    }
}