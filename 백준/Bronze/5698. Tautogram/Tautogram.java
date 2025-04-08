import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String S = scanner.nextLine().trim();
            if (S.equals("*")) {
                break;
            }
            String[] lst = S.split("\\s+");
            char a = '\0';
            boolean flag = true;
            for (String l : lst) {
                if (a == '\0') {
                    a = Character.toUpperCase(l.charAt(0));
                } else if (a != Character.toUpperCase(l.charAt(0))) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println("Y");
            } else {
                System.out.println("N");
            }
        }
        scanner.close();
    }
}