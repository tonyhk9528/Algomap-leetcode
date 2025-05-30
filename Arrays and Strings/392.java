public class 392 {
    class Solution {
        public boolean isSubsequence(String s, String t) {

            char[] needle = s.toCharArray();
            char[] haystack = s.toCharArray();
            int j = 0;

            while (j < needle.length) {

                for (int i = 0; i < haystack.length; i++) {

                    if ( haystack[i] == needle[j] ) {
                        j++;
                    }
                
                }

            } 

            return j == needle.length;
            
        }
    }
}
