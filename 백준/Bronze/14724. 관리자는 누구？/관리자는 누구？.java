import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] names = {"PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"};
        
        int N = sc.nextInt();
        sc.nextLine();
        
        int idx = 0, candidate = 0;
        for (int i = 0; i < 9; i++) {
            String[] inputLine = sc.nextLine().split(" ");
            int tmp = 0;
            for (String numStr : inputLine) {
                int c = Integer.parseInt(numStr);
                if (c > tmp) {
                    tmp = c;
                }
            }
            if (candidate < tmp) {
                candidate = tmp;
                idx = i;
            }
        }
        System.out.println(names[idx]);
        sc.close();
    }
}