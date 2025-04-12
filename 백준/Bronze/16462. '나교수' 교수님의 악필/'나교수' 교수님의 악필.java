import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        double x = 0;
        for (int i = 0; i < N; i++) {
            String Q = scanner.nextLine();
            StringBuilder s = new StringBuilder();
            for (char q : Q.toCharArray()) {
                if (q == '0' || q == '6' || q == '9') {
                    s.append('9');
                } else {
                    s.append(q);
                }
            }
            int num = Integer.parseInt(s.toString());
            x += Math.min(num, 100);
        }
        x /= N;
        int result = (x % 1 >= 0.5) ? (int)x + 1 : (int)x;
        System.out.println(result);
    }
}