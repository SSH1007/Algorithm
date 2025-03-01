import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] friend = new int[N];
        int[] target = new int[M];
        for (int i = 0; i < M; i++) {
            target[i] = sc.nextInt();
        }

        for (int m = 0; m < M; m++) {
            int tmp = 0;
            int miss = 0;
            int[] lst = new int[N];

            for (int n = 0; n < N; n++) {
                lst[n] = sc.nextInt();
                if (lst[n] == target[m]) {
                    friend[n]++;
                } else {
                    miss++;
                }
            }
            friend[target[m] - 1] += miss;
        }
        for (int i = 0; i < N; i++) {
            System.out.println(friend[i]);
        }
        sc.close();
    }
}