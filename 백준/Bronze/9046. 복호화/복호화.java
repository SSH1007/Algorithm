import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        
        for (int t = 0; t < N; t++) {
            String S = sc.nextLine().replace(" ", "");
            int[] alpha = new int[26];
            
            for (int i = 0; i < S.length(); i++) {
                char c = S.charAt(i);
                    alpha[c - 'a']++;
            }
            
            int maxN = 0;
            int dap = -1;
            for (int i = 0; i < 26; i++) {
                if (alpha[i] > maxN) {
                    maxN = alpha[i];
                    dap = i;
                }
            }
            
            int cnt = 0;
            for (int i = 0; i < 26; i++) {
                if (alpha[i] == maxN) {
                    cnt++;
                }
            }
            
            if (cnt > 1) {
                System.out.println("?");
            } else {
                System.out.println((char) (dap + 'a'));
            }
        }
        sc.close();
    }
}