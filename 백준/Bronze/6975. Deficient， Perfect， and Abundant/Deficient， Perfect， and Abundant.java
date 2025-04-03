import java.util.Scanner;

public class Main {
    public static int F(int X) {
        int sum = 0;
        for (int i = 1; i <= X / 2; i++) {
            if (X % i == 0) {
                sum += i;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        for (int n = 0; n < N; n++) {
            if (n > 0) {
                System.out.println();
            }
            int X = Integer.parseInt(sc.nextLine());
            int sum = F(X);
            if (sum > X) {
                System.out.println(X + " is an abundant number.");
            } else if (sum == X) {
                System.out.println(X + " is a perfect number.");
            } else {
                System.out.println(X + " is a deficient number.");
            }
        }
        sc.close();
    }
}