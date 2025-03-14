class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        int n = words[0].length();
        int totalWordsLen = words.length * n;
        
        List<Integer> answer = new ArrayList<>();

        // 초기화
        HashMap<String, Integer> wordsMap = new HashMap<>();
        for(String word : words) {
            wordsMap.put(word, wordsMap.getOrDefault(word, 0) + 1);
        }

        for(int i = 0; i < n; i++) { 
            int delete = i; // 맨 앞 단어 삭제를 위함
            int createCnt = (s.length() - i) / n; // 현재 문자열에서 만들 수 있는 총 개수
            Map<String, Integer> compareMap = new HashMap<>(); 
            
            for(int j = 0; j < words.length && (j+1) * n + i <= s.length(); j++) {
                int start = i + j * n;
                int end = (j+1) * n + i;
                String now = s.substring(start, end);

                compareMap.put(now, compareMap.getOrDefault(now, 0) + 1);
            }

            if(wordsMap.equals(compareMap)) {
                answer.add(i);
            }
             
            // 윈도우 이동
            for(int j = words.length; j < createCnt; j++) {
                String deleteKey = s.substring(delete, delete+n);
                int newVal = compareMap.get(deleteKey) - 1;

                if(newVal > 0) {
                    compareMap.put(deleteKey, newVal);
                }
                else {
                    compareMap.remove(deleteKey);   
                }

                delete+=n;

                int start = i + j * n;
                int end = (j+1) * n + i;
                String now = s.substring(start, end);

                compareMap.put(now, compareMap.getOrDefault(now, 0) + 1);

                if(wordsMap.equals(compareMap)) {
                    answer.add(i + ((j-words.length+1)*n));
                }
            }
        }

        return answer;
    }

}