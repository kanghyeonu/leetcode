class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> mergedList = new ArrayList<>();

        int idx1 = 0, idx2 = 0;
        while (idx1 < nums1.length || idx2 < nums2.length){
            int n1 = 0, n2 = 0;
            if (idx1 < nums1.length && idx2 < nums2.length){
                n1 = nums1[idx1];
                n2 = nums2[idx2];
            } else if (idx1 >= nums1.length){
                n2 = nums2[idx2];
                n1 = n2 + 1;
            } else if (idx2 >= nums2.length){
                n1 = nums1[idx1];
                n2 = n1 + 1;
            }

            if (n1 >= n2){
                mergedList.add(n2);
                idx2 += 1;
            } 
            else{
                mergedList.add(n1);
                idx1 += 1;
            }
        }

        int m = mergedList.size()/2;
        double answer;
        if (mergedList.size() % 2 == 0){
            answer = (mergedList.get(m) + mergedList.get(m-1))/2.0;
        } else {
            answer = mergedList.get(m);
        }

        return answer;
    }
}