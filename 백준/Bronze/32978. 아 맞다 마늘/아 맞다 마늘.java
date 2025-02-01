import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();

        Set<String> Ns = new HashSet<>();
        String[] list1 = sc.nextLine().split(" ");
        for (String item : list1) {
            Ns.add(item);
        }

        Set<String> H = new HashSet<>();
        String[] list2 = sc.nextLine().split(" ");
        for (String item : list2) {
            H.add(item);
        }

        Ns.removeAll(H);
        
        for (String item : Ns) {
            System.out.print(item + " ");
        }
        
        sc.close();
    }
}
