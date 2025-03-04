import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int C = Integer.parseInt(scanner.nextLine());
        int dap = 0;
        
        for (int i = 0; i < C; i++) {
            String code = scanner.nextLine();
            int tmp = 0;
            int j = 0;
            
            while (j < code.length()) {
                if (j + 3 <= code.length() && code.substring(j, j + 3).equals("for")) {
                    tmp++;
                    j += 3;
                } else if (j + 5 <= code.length() && code.substring(j, j + 5).equals("while")) {
                    tmp++;
                    j += 5;
                } else {
                    j++;
                }
            }
            dap = Math.max(dap, tmp);
        }
        System.out.println(dap);
        scanner.close();
    }
}