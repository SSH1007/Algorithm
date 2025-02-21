import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        scanner.close();
        if (m == 0) {
            System.out.println(0);
            return;
        }

        List<Integer> lst = new ArrayList<>();
        while (m > 1) {
            lst.add(m % n);
            m /= n;
        }
        if (m > 0) {
            lst.add(m);
        }

        StringBuilder result = new StringBuilder();
        for (int i = lst.size() - 1; i >= 0; i--) {
            if (lst.get(i) > 9) {
                result.append((char) (lst.get(i) + 55)); 
            } else {
                result.append(lst.get(i));
            }
        }
        System.out.println(result);
    }
}