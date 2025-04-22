import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int dap = 0, cnt = 0;
        List<int[]> lst = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            if (A < N) {
                lst.add(new int[]{A, B});
            } else {
                cnt++;
            }
        }
        lst.sort((a, b) -> Integer.compare(a[0], b[0]));
        while (cnt < M - 1) {
            int[] tmp = lst.remove(lst.size() - 1);
            int tmpA = tmp[0];
            int tmpB = tmp[1];
            while (tmpA < N) {
                tmpA++;
                tmpB--;
                dap++;
            }
            cnt++;
        }
        System.out.println(dap);
    }
}