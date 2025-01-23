import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String S = br.readLine();
        int[] alp = new int[26];
        for (int n = 0; n < N; n++) {
            char c = S.charAt(n);
            if (Character.isAlphabetic(c)) {
                alp[Character.toLowerCase(c) - 'a']++;
            }
        }
        int maxIndex = 0;
        for (int i = 1; i < 26; i++) {
            if (alp[i] > alp[maxIndex]) {
                maxIndex = i;
            }
        }
        System.out.println(alp[maxIndex]);
    }
}