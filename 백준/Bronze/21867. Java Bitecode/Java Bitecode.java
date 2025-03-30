import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String S = sc.nextLine();
        StringBuilder result = new StringBuilder();
        for (int n = 0; n < N; n++) {
            char ch = S.charAt(n);
            if (ch != 'J' && ch != 'A' && ch != 'V') {
                result.append(ch);
            }
        }
        if (result.length() > 0) {
            System.out.println(result.toString());
        } else {
            System.out.println("nojava");
        }
        sc.close();
    }
}