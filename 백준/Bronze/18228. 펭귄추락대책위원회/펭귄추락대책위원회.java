import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
    
        int[] As = new int[N];
        for (int i = 0; i < N; i++) {
            As[i] = sc.nextInt();
        }

        int penguin = 0;
        for (int i = 0; i < N; i++) {
            if (As[i] == -1) {
                penguin = i;
                break;
            }
        }

        int minLeft = Integer.MAX_VALUE;
        int minRight = Integer.MAX_VALUE;
        for (int i = 0; i < penguin; i++) {
            minLeft = Math.min(minLeft, As[i]);
        }
        for (int i = penguin + 1; i < N; i++) {
            minRight = Math.min(minRight, As[i]);
        }
        System.out.println(minLeft + minRight);
        sc.close();
    }
}