import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger A = sc.nextBigInteger();
        BigInteger B = sc.nextBigInteger();
        BigInteger C = sc.nextBigInteger();
        if (C.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO)) {
            System.out.println(A);
        } else {
            System.out.println(A.xor(B));
        }
        sc.close();
    }
}