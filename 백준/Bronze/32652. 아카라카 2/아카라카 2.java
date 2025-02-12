import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int K = scanner.nextInt();
        String a = "AKA";
        String result = a + "RAKA".repeat(K);
        System.out.println(result);
        scanner.close();
    }
}