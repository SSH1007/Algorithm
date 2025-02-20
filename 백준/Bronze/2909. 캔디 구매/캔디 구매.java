import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();
        int K = sc.nextInt();
        int t = C % (int) Math.pow(10, K);
        if (t >= Math.pow(10, K)/2) {
            C += (int) Math.pow(10, K);
        }
        C -= t;
        System.out.println(C);
        sc.close();
    }
}