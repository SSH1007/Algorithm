import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        sc.nextLine();
        String S = sc.nextLine();
        String g = "gori";
        
        for (int n = 0; n <= N - 4; n++) {
            if (S.substring(n, n + 4).equals(g)) {
                System.out.println("YES");
                return;
            }
        }
        
        System.out.println("NO");
    }
}
