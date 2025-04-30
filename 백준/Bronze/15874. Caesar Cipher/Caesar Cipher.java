import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int s = sc.nextInt();
        sc.nextLine();
        String S = sc.nextLine();
        StringBuilder dap = new StringBuilder();
        for (int i = 0; i < s; i++) {
            char ch = S.charAt(i);
            if (Character.isLetter(ch)) {
                if (Character.isUpperCase(ch)) {
                    dap.append((char)((ch - 'A' + k) % 26 + 'A'));
                } else {
                    dap.append((char)((ch - 'a' + k) % 26 + 'a'));
                }
            } else {
                dap.append(ch);
            }
        }
        System.out.println(dap.toString());
        sc.close();
    }
}