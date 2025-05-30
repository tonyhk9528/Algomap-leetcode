public class 1768 {
    class Solution {
        public String mergeAlternately(String word1, String word2) {
            int length; 
            StringBuilder answerBuilder = new StringBuilder();
            boolean word2Longer = false;

            if (word1.length() >= word2.length()) length = word2.length(); else { length = word1.length(); word2Longer = true; }

            for (int i = 0; i < length; i++) {
                
                answerBuilder.append(word1.charAt(i));
                answerBuilder.append(word2.charAt(i));
            }

            if (word2Longer) {

                answerBuilder.append(word2.substring(length, word2.length()));

            } else if (word1.length() != word2.length()) {

                answerBuilder.append(word2.substring(length, word1.length()));

            }

            return answerBuilder.toString();
            
        }
        
    }
}
