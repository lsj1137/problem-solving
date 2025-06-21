import java.util.*;

class Solution {
    public String changeSharp(String melody) {
        melody = melody.replaceAll("A#", "H");
        melody = melody.replaceAll("C#", "I");
        melody = melody.replaceAll("D#", "J");
        melody = melody.replaceAll("F#", "K");
        melody = melody.replaceAll("G#", "L");
        melody = melody.replaceAll("B#", "M");
        return melody;
    }
    
    public int toMinute(String time) {
        String[] hourMinute = time.split(":");
        int hour = Integer.valueOf(hourMinute[0]);
        int minute = Integer.valueOf(hourMinute[1]);
        return hour*60 + minute;
    }
    
    public String toBroadcasted (int time, String melody) {
        String result = "";
        int i = 0;
        while (result.length() < time) {
            result += melody.charAt(i);
            i = (i+1) % melody.length();
        }
        return result;
    }
    
    public boolean isThisSong(String origin, String heard) {
        int correct = 0;
        int index = 0;
        for (int i=0; i<origin.length(); i++) {
            if (origin.charAt(i) == heard.charAt(index)) {
                index += 1;
                correct += 1;
                if (correct==heard.length()) break;
            } else {
                index = 0;
                correct = 0;
                if (origin.charAt(i) == heard.charAt(index)) {
                    index += 1;
                    correct += 1;
                    if (correct==heard.length()) break;
                }
            }
        }
        return correct==heard.length();
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        String tempAnswer = "";
        String M = changeSharp(m);
        for (String info: musicinfos) {
            String[] data = info.split(",");
            int start = toMinute(data[0]);
            int end = toMinute(data[1]);
            data[3] = changeSharp(data[3]);
            // System.out.printf("%d ~ %d\n", start, end);
            String broadcastedSong = toBroadcasted(end-start, data[3]);
            // System.out.println(broadcastedSong);
            if (isThisSong(broadcastedSong, M)) {
                if (tempAnswer.equals("")) {
                    tempAnswer = Integer.toString(end-start) + "," + data[2];
                } else {
                    String[] tempData = tempAnswer.split(",");
                    int time = Integer.parseInt(tempData[0]);
                    if (time < end-start) {
                        tempAnswer = Integer.toString(end-start) + "," + data[2];
                    }
                }
            }
        }
        if (tempAnswer.equals("")) {
            answer = "(None)";
        } else {
            answer = tempAnswer.split(",")[1];
        }
        return answer;
    }
}