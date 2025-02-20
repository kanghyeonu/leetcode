class Solution {
    public boolean isValid(String s) {
        if (s.length()%2 != 0){
            return false;
        }

        Stack<Character> st = new Stack<>();
        Map<Character, Character> hashMap = new HashMap<>();
        hashMap.put(')', '(');
        hashMap.put('}', '{');
        hashMap.put(']', '[');

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '['){
                st.push(s.charAt(i));
            } else {
                if (st.isEmpty() || hashMap.get(s.charAt(i)) != st.pop()){
                    return false;
                }
            }
        }

        return (st.isEmpty()) ? true : false;
    }
}