import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Character> lst = Arrays.asList('r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g');
    
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        String S = scanner.nextLine();
        if (lst.contains(S.charAt(S.length() - 1))) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        scanner.close();
    }
}