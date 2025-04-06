import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] lst = new int[N][3];
        for (int i = 0; i < N; i++) {
            lst[i][0] = scanner.nextInt();
            lst[i][1] = scanner.nextInt();
            lst[i][2] = scanner.nextInt();
        }
        int dap = 0;
        for (int i = 1; i <= 3; i++) {
            int tmp = 0;
            int current = i;
            for (int n = 0; n < N; n++) {
                int a = lst[n][0];
                int b = lst[n][1];
                int g = lst[n][2];
                if (current == a) {
                    current = b;
                } else if (current == b) {
                    current = a;
                }
                if (current == g) {
                    tmp++;
                }
            }
            dap = Math.max(dap, tmp);
        }
        System.out.println(dap);
        scanner.close();
    }
}