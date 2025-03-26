import java.util.Scanner;

public class Main {
    public static boolean check(int n) {
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String O = sc.next();
        String N = sc.next();
        boolean A = check(Integer.parseInt(O));
        boolean B = check(Integer.parseInt(N + O));
        if (A == B) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        sc.close();
    }
}