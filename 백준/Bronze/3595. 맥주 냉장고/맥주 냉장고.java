import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        double dap = Double.MAX_VALUE;
        int a = 0, b = 0, c = 0;

        for (int n = 1; n <= N; n++) {
            if (N % n == 0) {
                for (int m = 1; m <= N / n; m++) {
                    if ((N / n) % m == 0) {
                        int o = N / n / m;
                        double current = 2 * (n * m + m * o + n * o);
                        if (dap > current) {
                            dap = current;
                            a = n;
                            b = m;
                            c = o;
                        }
                    }
                }
            }
        }
        System.out.println(a + " " + b + " " + c);
        sc.close();
    }
}