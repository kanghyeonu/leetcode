import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        Map<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i ++){
            int num = nums[i];
            if (hashMap.containsKey(target - num)){
                answer[0] = hashMap.get(target - num);
                answer[1] = i;
                return answer;
            }
            hashMap.put(nums[i], i);
        }
        return answer;
    }   
}