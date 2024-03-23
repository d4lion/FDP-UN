import java.util.Scanner;
import java.lang.Math;;

public class i_ejercicio_9 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        double L = Double.parseDouble(scanner.next());
        double D = Double.parseDouble(scanner.next());

        scanner.close();

        double L2 = Math.sqrt(Math.pow(D, 2) - Math.pow(L, 2));

        double result = L * L2;

        System.out.format("%.2f", result);
        
    }
}