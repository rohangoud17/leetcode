class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> myHashMap = new HashMap<>();
        for(String word: strs){
            char[] arr = word.toCharArray();
            Arrays.sort(arr);
            String sortedWord = new String(arr);
            if(!(myHashMap.containsKey(sortedWord))){
                myHashMap.put(sortedWord,new ArrayList<String>());
            }
            myHashMap.get(sortedWord).add(word);
        }
        return new ArrayList<>(myHashMap.values());
    }
}