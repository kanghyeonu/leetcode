class Solution {
    private List<String> answer = new ArrayList<>();
    private Map<String, String> hashMap = new HashMap<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0){
            return answer;
        }
        hashMap.put("2", "abc");
        hashMap.put("3", "def");
        hashMap.put("4", "ghi");
        hashMap.put("5", "jkl");
        hashMap.put("6", "mno");
        hashMap.put("7", "pqrs");
        hashMap.put("8", "tuv");
        hashMap.put("9", "wxyz");

        dfs(digits, 0, "");
        return answer;

    }

    void dfs(String num, int index, String comb){
        if (index == num.length()){
            answer.add(comb);
            return;
        }
        String str = hashMap.get(String.valueOf(num.charAt(index)));
        for (int i = 0; i < str.length(); i++){
            dfs(num, index+1, comb + String.valueOf(str.charAt(i)));
        }
    }
}