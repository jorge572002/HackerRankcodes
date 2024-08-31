package JavaProblems;
import java.util.Scanner;

public class JavaOutputFormating {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("================================");
        for(int i=0;i<3;i++){
            String s1=sc.next();
            int x=sc.nextInt();
            String nuevo= Integer.toString(x);
            while (nuevo.length() < 3){
                nuevo = "0" + nuevo;
            }
            while (s1.length() < 15){
                s1 = s1 + ' ';
            }
            //Complete this line
            System.out.println(s1 + nuevo);
        }
        System.out.println("================================");

}
}

