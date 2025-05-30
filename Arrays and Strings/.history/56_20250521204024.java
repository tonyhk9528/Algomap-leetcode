import java.util.Arrays;

public class 56 {
    class Solution {
        public int[][] merge(int[][] intervals) {
            // Step 1: Sort intervals by starting time
            Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));


            int n = intervals.length;
            int l = 0;
            int[][] temp = new int[n][2];
            int[] interval = intervals[0];

            for (int i = 1; i < n; i++) {
                if ( interval[0] <= intervals[i][0] && intervals[i][0] <= interval[1] ){
                    interval[1] = Math.max(intervals[i][1], interval[1]);
                } else {
                    temp[l] = interval;
                    interval = intervals[i];
                    l++;
                }
            }

            temp[l] = interval;
            l++;

            int[][] answer = new int[l][2];

            for (int i = 0; i < l; i++) {
                answer[i] = temp[i];
            }

            return answer;
        }
    }
}

//
//[[1,3],[2,6],[8,10],[15,18]]
