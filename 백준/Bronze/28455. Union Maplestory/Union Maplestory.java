import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] L = new int[N];
        for (int i = 0; i < N; i++) {
            L[i] = sc.nextInt();
        }
        Arrays.sort(L);
        for (int i = 0; i < N / 2; i++) {
            int temp = L[i];
            L[i] = L[N - i - 1];
            L[N - i - 1] = temp;
        }
        int[] lvs = {60, 100, 140, 200, 250};
        int hap = 0, up = 0;
        for (int i = 0; i < 42; i++) {
            if (i >= N) break;
            for (int lv : lvs) {
                if (L[i] >= lv) {
                    up++;
                }
            }
            hap += L[i];
        }
        System.out.println(hap + " " + up);
    }
}