package JavaProblems;
import java.util.Scanner;

public class StdinStdout{

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int i = scan.nextInt();
        double d = scan.nextDouble();
        //dummy to avoid the blanck space after previous scan
        String dummy = scan.nextLine();
        String s = scan.nextLine();

        // Write your code here.

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}