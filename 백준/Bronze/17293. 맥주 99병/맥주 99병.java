import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        
        for (int n = N; n > 0; n--) {
            String b = (n == 1) ? "bottle" : "bottles";
            String nb = (n - 1 == 1) ? "bottle" : "bottles";
            
            System.out.println(n + " " + b + " of beer on the wall, " + n + " " + b + " of beer.");
            if (n > 1) {
                System.out.println("Take one down and pass it around, " + (n - 1) + " " + nb + " of beer on the wall.");
            } else {
                System.out.println("Take one down and pass it around, no more bottles of beer on the wall.");
            }
            System.out.println();
        }

        System.out.println("No more bottles of beer on the wall, no more bottles of beer.");
        System.out.println("Go to the store and buy some more, " + N + " " + (N == 1 ? "bottle" : "bottles") + " of beer on the wall.");
        scanner.close();
    }
}