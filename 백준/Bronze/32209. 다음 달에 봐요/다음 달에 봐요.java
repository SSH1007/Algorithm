import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int Q = sc.nextInt();
        int q = 0;

        for (int i = 0; i < Q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (a % 2 != 0) {
                q += b;
            } else {
                q -= b;
            }

            if (q < 0) {
                System.out.println("Adios");
                return;
            }
        }

        System.out.println("See you next month");
    }
}
