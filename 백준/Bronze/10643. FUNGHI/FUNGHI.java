import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] pizza = new int[8];
        for (int i = 0; i < 8; i++) {
            pizza[i] = sc.nextInt();
        }
        int maxSum = 0;
        for (int i = 0; i < 8; i++) {
            int tempSum = 0;
            for (int j = 0; j < 4; j++) {
                int index = (i + j) % 8;
                tempSum += pizza[index];
            }
            maxSum = Math.max(maxSum, tempSum);
        }
        System.out.println(maxSum);
        sc.close();
    }
}