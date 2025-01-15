import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long tmp = 1;

        for (int i = N-4; i <= N; i++){
            tmp *= i;
        }

        System.out.println(tmp/120);
    }
}