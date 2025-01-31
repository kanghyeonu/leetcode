class Solution {
    public String convert(String s, int numRows) {
        List<Integer> cycle = new ArrayList<>();
        List<String> rows = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++){
            cycle.add(i);
        }
        for (int i = numRows - 2; i >= 1; i--){
            cycle.add(i);
        }
        for (int i = 0; i < numRows; i++){
            rows.add("");
        }

        System.out.print(cycle);
        int c = cycle.size();
        for (int i = 0; i < s.length(); i++){
            rows.set(cycle.get(i%c), rows.get(cycle.get(i%c)) + s.charAt(i));
        }

        String answer = String.join("", rows);
        return answer;
    }
}