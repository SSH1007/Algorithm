import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        
        for (int i = 0; i < N; i++) {
            String S = scanner.nextLine();
            StringBuilder reversed = new StringBuilder(S);
            System.out.println(reversed.reverse().toString());
        }
        
        scanner.close();
    }
}
