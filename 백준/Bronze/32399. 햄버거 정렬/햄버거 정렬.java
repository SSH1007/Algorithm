import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.nextLine();
        
        if (S.equals("(1)")){
            System.out.println(0);
        } else if (S.equals(")1(")){
            System.out.println(2);
        } else {
            System.out.println(1);
        }
        
        scanner.close();
    }
}