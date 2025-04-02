import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String N = sc.nextLine();
        int L = N.length();
        long num = Long.parseLong(N);
        long dap = 0;
        for (int i = 0; i < L; i++) {
            long a = num % 10;
            long b = num / 10;
            long powerOfTen = 1;
            for (int j = 0; j < L - 1; j++) {
                powerOfTen *= 10;
            }
            num = b + a * powerOfTen;
            dap += b + a * powerOfTen;
        }
        System.out.println(dap);
        sc.close();
    }
}