import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a == 0){
            System.out.println((int)Math.pow(c, 2)-b);
        }
        else if (b == 0) {
            System.out.println((int)Math.pow(c,2)-a);
        }
        else {
            System.out.println((int)Math.sqrt(a+b));
        }
    }

}