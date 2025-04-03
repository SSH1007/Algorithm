import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int[] Ps = new int[N];
        int sum = 0;
        for (int i = 0; i < N; i++) {
            Ps[i] = sc.nextInt();
            sum += Ps[i];
        }
        if (sum % X == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        sc.close();
    }
}