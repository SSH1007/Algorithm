import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String mascot = br.readLine();
        int K = Integer.parseInt(br.readLine());

        if (mascot.equals("induck")) {
            if (K % 2 == 0) {
                System.out.println(K);
            } else {
                if (K + 1 > N) {
                    System.out.println(K - 1);
                } else {
                    System.out.println(K + 1);
                }
            }
        } else {
            if (K % 2 == 1) {
                System.out.println(K);
            } else {
                if (K + 1 > N) {
                    System.out.println(K - 1);
                } else {
                    System.out.println(K + 1);
                }
            }
        }

        br.close();
    }
}
