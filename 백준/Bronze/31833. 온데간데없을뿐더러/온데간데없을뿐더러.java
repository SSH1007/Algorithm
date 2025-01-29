import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        String[] As = br.readLine().split(" ");
        String[] Bs = br.readLine().split(" ");
        StringBuilder A = new StringBuilder();
        StringBuilder B = new StringBuilder();
        for (String a : As) {
            A.append(a);
        }
        for (String b : Bs) {
            B.append(b);
        }
        long aNum = Long.parseLong(A.toString());
        long bNum = Long.parseLong(B.toString());
        if (aNum >= bNum) {
            System.out.println(B);
        } else {
            System.out.println(A);
        }
    }
}
