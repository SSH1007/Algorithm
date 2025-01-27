import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        int W = Integer.parseInt(reader.readLine());
        
        System.out.println((int) (Math.sqrt(W / 2)) * 8);
    }
}
