import java.util.HashMap;

public class 13 {
    class Solution {
        public int romanToInt(String s) {
            HashMap<Character, Integer> map = new HashMap<>();

            map.put('I', 1);
            map.put('V', 5);
            map.put('X', 10);
            map.put('L', 50);
            map.put('C', 100);
            map.put('D', 500);
            map.put('M', 1000);


            int answer = 0;

            char[] sArray = s.toCharArray(); 

            for (int i = 0; i < sArray.length - 1; i++) {

                if ( map.get(sArray[i]) >= map.get(sArray[i + 1]) ) {
                    answer += map.get(sArray[i]);
                } else {
                    answer -= map.get(sArray[i]);
                }

                
            }

            answer += map.get(sArray[sArray.length]);
            

            return answer;
        }
    }
}




