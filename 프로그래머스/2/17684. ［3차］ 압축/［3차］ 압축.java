import java.util.*;

class Solution {
    public int[] solution(String msg) {
        int[] answer = {};
        ArrayList<Integer> tempAnswer = new ArrayList<Integer>();
        HashMap<String, Integer> dictionary = new HashMap<String, Integer>();
        dictionary.put("", 0);
        dictionary.put("A", 1);
        dictionary.put("B", 2);
        dictionary.put("C", 3);
        dictionary.put("D", 4);
        dictionary.put("E", 5);
        dictionary.put("F", 6);
        dictionary.put("G", 7);
        dictionary.put("H", 8);
        dictionary.put("I", 9);
        dictionary.put("J", 10);
        dictionary.put("K", 11);
        dictionary.put("L", 12);
        dictionary.put("M", 13);
        dictionary.put("N", 14);
        dictionary.put("O", 15);
        dictionary.put("P", 16);
        dictionary.put("Q", 17);
        dictionary.put("R", 18);
        dictionary.put("S", 19);
        dictionary.put("T", 20);
        dictionary.put("U", 21);
        dictionary.put("V", 22);
        dictionary.put("W", 23);
        dictionary.put("X", 24);
        dictionary.put("Y", 25);
        dictionary.put("Z", 26);
        int wordIndex = 27;
        int index = 0;
        String checkWord = "";
        int encoded = 0;
        while (index < msg.length()){
            while (dictionary.containsKey(checkWord) && index<msg.length()) {
                encoded = dictionary.get(checkWord);
                checkWord += msg.charAt(index);
                index += 1;
            }
            if (!dictionary.containsKey(checkWord)) {
                tempAnswer.add(encoded);
                dictionary.put(checkWord, wordIndex++);
                checkWord = Character.toString(msg.charAt(index-1));
                if (index == msg.length()) {
                    encoded = dictionary.get(checkWord);
                    tempAnswer.add(encoded);
                }
            } else {
                encoded = dictionary.get(checkWord);
                tempAnswer.add(encoded);
            }
        }
        answer = new int[tempAnswer.size()];
        int i = 0;
        for (int a: tempAnswer) {
            answer[i++] = a;
        }
        return answer;
    }
}