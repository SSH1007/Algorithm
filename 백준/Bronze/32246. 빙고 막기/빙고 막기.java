import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n==2){
            System.out.println(3);
        } else {
            System.out.println(n);
        }
        sc.close();
    }
}