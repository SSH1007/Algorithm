import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < N; i++) {
            String S = scanner.nextLine();
            if (S.startsWith("Simon says")) {
                System.out.println(S.substring(10));
            }
        }
        scanner.close();
    }
}