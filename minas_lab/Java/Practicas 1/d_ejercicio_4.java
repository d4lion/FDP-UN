import java.util.Scanner;


public class d_ejercicio_4 {
    public static void main(String[] args){
        
        Scanner scanner = new Scanner(System.in);
        
        double B, b, h;

        B = Double.parseDouble(scanner.next());
        b = Double.parseDouble(scanner.next());
        h = Double.parseDouble(scanner.next());

        scanner.close();

        double area_total = (b * h) + ((B-b)/2.0) * h;

        System.out.println(area_total);
    }
}
