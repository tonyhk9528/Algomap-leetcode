import java.util.ArrayList;
import java.util.List;

public class 238 {
    class Solution {
        public List<String> summaryRanges(int[] nums) {

            StringBuilder range = new StringBuilder();
            ArrayList answer = new ArrayList();

            if (nums.length <= 0) {
                return answer;
            }

            int prev = nums[0];
            

            range.append(String.valueOf(prev));


            for (int i = 1; i < nums.length; i++) {

                if (nums[i] - prev != 1) {
                    
                    if (range.toString().contains("->")) {
                        range.append(String.valueOf(prev));
                    }

                    answer.add(range.toString());
                    range.setLength(0);
                    range.append(nums[i]);
                    

                } else {
                    if (!range.toString().contains("->")){
                        range.append("->");
                    }
                }

                prev = nums[i];
            }

            if (!range.toString().equals(String.valueOf(prev))) {
                range.append(String.valueOf(prev));
            } 
            
            answer.add(range.toString());

    
            return answer;
        }
    }
}
