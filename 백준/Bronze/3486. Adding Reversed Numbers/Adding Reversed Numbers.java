import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static int F(int n) {
        int res = 0;
        while (n > 0) {
            res = res * 10 + (n % 10);
            n /= 10;
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int revA = F(A);
            int revB = F(B);
            int tmp = revA + revB;
            System.out.println(F(tmp));
        }
    }
}