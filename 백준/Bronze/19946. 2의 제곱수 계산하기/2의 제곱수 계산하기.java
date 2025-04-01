import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger N = sc.nextBigInteger();
        int cnt = 1;
        boolean flag = false;
        while (N.compareTo(BigInteger.valueOf(2)) > 0) {
            if (N.mod(BigInteger.TWO).equals(BigInteger.ONE)) {  // N이 홀수일 때
                N = N.add(BigInteger.ONE);
                flag = true;
                cnt = 1;
            }
            N = N.divide(BigInteger.TWO);
            if (flag) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
        sc.close();
    }
}