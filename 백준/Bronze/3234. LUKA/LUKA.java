import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        sc.nextLine();
        int K = sc.nextInt();
        sc.nextLine(); 
        String S = sc.nextLine();
        
        List<Integer> lst = new ArrayList<>();
        int x = 0, y = 0;
        if (Math.abs(X - x) <= 1 && Math.abs(Y - y) <= 1) {
            lst.add(0);
        }
        for (int k = 0; k < K; k++) {
            char c = S.charAt(k);
            if (c == 'I') {
                x += 1;
            } else if (c == 'S') {
                y += 1;
            } else if (c == 'Z') {
                x -= 1;
            } else {
                y -= 1;
            }
            if (Math.abs(X - x) <= 1 && Math.abs(Y - y) <= 1) {
                lst.add(k + 1);
            }
        }
        if (lst.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int num : lst) {
                System.out.println(num);
            }
        }
        sc.close();
    }
}