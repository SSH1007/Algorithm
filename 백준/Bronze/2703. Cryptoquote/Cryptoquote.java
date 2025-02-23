import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = Integer.parseInt(scanner.nextLine());

        for (int t = 0; t < T; t++) {
            String cipher = scanner.nextLine();
            String rule = scanner.nextLine();
            
            StringBuilder result = new StringBuilder();

            for (int i = 0; i < cipher.length(); i++) {
                char c = cipher.charAt(i);
                if (c == ' ') {
                    result.append(' ');
                } else {
                    result.append(rule.charAt(c - 'A'));
                }
            }

            System.out.println(result);
        }
        scanner.close();
    }
}