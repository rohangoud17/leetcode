class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> resultList = new ArrayList<>();
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int i: nums){
            int count = countMap.getOrDefault(i, 0);
            countMap.put(i, count + 1);
            if(count == 1){
                resultList.add(i);
            }
        }  
    return resultList;
    }
}