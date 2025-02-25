import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] board = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            board[i] = sc.nextInt();
        }

        int cur = 1;
        for (int j = 1; j <= M; j++) {
            int D = sc.nextInt();
            cur += D;
            if (cur >= N) {
                System.out.println(j);
                return;
            }
            cur += board[cur];
            if (cur >= N) {
                System.out.println(j);
                return;
            }
        }
        sc.close();
    }
}