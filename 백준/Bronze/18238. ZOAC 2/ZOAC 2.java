import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String S = input;
        int start = 0;
        int acc = 0;
        for (int i = 0; i < S.length(); i++) {
            char s = S.charAt(i);
            int c = s - 'A';
            int m = (start - c + 26) % 26;
            int n = 26 - m;
            acc += Math.min(m, n);
            start = c;
        }
        System.out.println(acc);
    }
}