import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();
            int a = 1;
            for (int n = 1; n <= N; n++) {
                a *= n;
                while (a % 10 == 0) {
                    a /= 10;
                }
                a %= 10000;
            }
            System.out.println(a % 10);
        }
        sc.close();
    }
}