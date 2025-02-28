import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = Math.min(a, b);
        
        for (int i = 1; i <= c; i++) {
            if (a % i == 0 && b % i == 0) {
                System.out.println(i + " " + (a / i) + " " + (b / i));
            }
        }
        scanner.close();
    }
}