import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {
            String inp = br.readLine();
            if (inp == null || inp.trim().isEmpty()) {
                break;
            }
            
            String[] parts = inp.split(" ");
            double N = Double.parseDouble(parts[0]);
            double B = Double.parseDouble(parts[1]);
            double M = Double.parseDouble(parts[2]);
            
            int year = 0;
            while (N <= M) {
                N += N * B / 100;
                year++;
            }
            System.out.println(year);
        }
        br.close();
    }
}