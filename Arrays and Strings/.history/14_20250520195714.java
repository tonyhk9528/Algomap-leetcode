public class 14 {
    class Solution {
        public String longestCommonPrefix(String[] strs) {
            StringBuilder answer = new StringBuilder();

            for (int i = 0; i < strs[0].toCharArray().length; i++) {

                for (int j = 1; i < strs.length; j++) {
                    if (strs[j].length() == i) {
                        return answer.toString();
                    }

                    if (strs[0].toCharArray()[i] != strs[j].toCharArray()[i]) {
                        return answer.toString();
                    }
                }
                answer.append(strs[0].toCharArray()[i]);
            }

            return answer.toString();
                
        }            
    }
}

