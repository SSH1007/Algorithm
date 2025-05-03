import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int totalLength = 0;
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            totalLength += line.length();
        }
        System.out.println(totalLength);
    }
}