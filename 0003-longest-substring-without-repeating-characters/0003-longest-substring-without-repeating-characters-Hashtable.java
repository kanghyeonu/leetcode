class Solution {
    public int lengthOfLongestSubstring(String s) {
        int answer = 0;
        Map<String, Integer> pos = new HashMap<>();
        int start = 0, end = 1;

        for (int i = 0; i < s.length(); i++){
            String ch = s.substring(i, i+1);
            Integer lastEncounterPos = pos.get(ch);

            if (lastEncounterPos != null){
                start = Math.max(lastEncounterPos + 1, start);
            }
            end = i;
            pos.put(ch, i);

            if (answer < end - start + 1){
                answer = end - start + 1;
            }
        }

        return answer;
    }
}