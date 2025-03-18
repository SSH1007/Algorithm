import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
   
        int N = sc.nextInt();
        int[] As = new int[N];
        for (int i = 0; i < N; i++) {
            As[i] = sc.nextInt();
        }
        List<Integer> odd = new ArrayList<>();
        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (As[i] % 2 == 1) {
                odd.add(As[i]);
            } else {
                even.add(As[i]);
            }
        }
        int dap = 0;
        for (int num : even) {
            dap += num;
        }
        Collections.sort(odd);
        while (odd.size() > 1) {
            int a = odd.remove(odd.size() - 1);
            int b = odd.remove(odd.size() - 1);
            dap += (a + b);
        }
        System.out.println(dap);
        sc.close();
    }
}