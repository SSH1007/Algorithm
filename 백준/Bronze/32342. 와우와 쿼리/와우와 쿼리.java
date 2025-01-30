import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int Q = Integer.parseInt(br.readLine());
        
        for (int a = 0; a < Q; a++) {
            String S = br.readLine();
            int tmp = 0;
            
            for (int i = 0; i <= S.length() - 3; i++) {
                if (S.substring(i, i + 3).equals("WOW")) {
                    tmp++;
                }
            }
            
            System.out.println(tmp);
        }
    }
}
