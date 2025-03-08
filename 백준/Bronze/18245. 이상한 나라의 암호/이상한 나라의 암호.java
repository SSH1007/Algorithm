import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = 1;
        while (true) {
            String S = sc.nextLine();
            if (S.equals("Was it a cat I saw?")) {
                break;
            }
            for (int i = 0; i < S.length(); i += t + 1) {
                System.out.print(S.charAt(i));
            }
            System.out.println();
            t++;
        }
        sc.close();
    }
}