import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        if (n % 3 != 0 && m % 3 != 0) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
        sc.close();
    }
}