import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int dap = 0;
        for (int i = 0; i <= N; i++) {
            if (F(i, K)) {
                dap += 3600;
                continue;
            }
            for (int j = 0; j < 60; j++) {
                if (F(j, K)) {
                    dap += 60;
                    continue;
                }
                for (int k = 0; k < 60; k++) {
                    if (F(k, K)) {
                        dap++;
                    }
                }
            }
        }
        System.out.println(dap);
    }

    private static boolean F(int num, int target) {
        return num / 10 == target || num % 10 == target;
    }
}