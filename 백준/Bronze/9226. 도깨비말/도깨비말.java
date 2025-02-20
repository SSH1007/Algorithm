import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String vowels = "aeiou";
        while (true) {
            String S = scanner.nextLine();
            if (S.equals("#")) {
                break;
            }
            int idx = 0;
            for (int i = 0; i < S.length(); i++) {
                char c = S.charAt(i);
                if (vowels.indexOf(c) != -1) {
                    idx = i;
                    break;
                }
            }
            String result = S.substring(idx) + S.substring(0, idx) + "ay";
            System.out.println(result);
        }
        scanner.close();
    }
}