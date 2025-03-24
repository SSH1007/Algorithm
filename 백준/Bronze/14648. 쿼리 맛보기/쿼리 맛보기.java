import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        long[] y = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            y[i] = Integer.parseInt(st.nextToken());
        }
        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            if (type == 1) {
                int l = Integer.parseInt(st.nextToken()) - 1;
                int r = Integer.parseInt(st.nextToken());
                long sum = 0;
                for (int i = l; i < r; i++) {
                    sum += y[i];
                }
                System.out.println(sum);
                long temp = y[l];
                y[l] = y[r - 1];
                y[r - 1] = temp;
            } else {
                int l1 = Integer.parseInt(st.nextToken()) - 1;
                int r1 = Integer.parseInt(st.nextToken());
                int l2 = Integer.parseInt(st.nextToken()) - 1;
                int r2 = Integer.parseInt(st.nextToken());
                long sum1 = 0, sum2 = 0;
                for (int i = l1; i < r1; i++) {
                    sum1 += y[i];
                }
                for (int i = l2; i < r2; i++) {
                    sum2 += y[i];
                }
                System.out.println(sum1 - sum2);
            }
        }
    }
}