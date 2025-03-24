import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int i = 1;
        while (N > i) {
            N -= i;
            i++;
        }
        System.out.println((i + 1 - N) + " " + N);
        sc.close();
    }
}