import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String S = sc.nextLine();
            
            if (S.equals("#")) {
                break;
            }

            int dap = 0;
            for (int i = 0; i < S.length(); i++) {
                char ch = S.charAt(i);
                if (ch == ' ') {
                    continue;
                }
                dap += (ch - 'A' + 1) * (i + 1);
            }
            System.out.println(dap);
        }
        sc.close();
    }
}