import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String C = sc.nextLine();
            if (C.equals("0")) {
                break;
            } else {
                String[] parts = C.split(" ");
                int N = Integer.parseInt(parts[0]);
                int P = Integer.parseInt(parts[1]);

                int n = N / 2;
                int p = (P + 1) / 2;

                Set<Integer> dapSet = new TreeSet<>();
                dapSet.add(2 * p - 1);
                dapSet.add(2 * p);
                dapSet.add(2 * (n - p + 1));
                dapSet.add(2 * (n - p + 1) - 1);
                dapSet.remove(P);

                for (int num : dapSet) {
                    System.out.print(num + " ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}