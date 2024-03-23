import java.lang.Math;
import java.util.Scanner;

public class g_ejercicio_7 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int radio = Integer.parseInt(scanner.next());
        scanner.close();

        double PI = Math.PI;


        double perimetro = PI * 2 * radio;
        double area = PI * Math.pow(radio, 2);
        double volumen = 4.0/3.0 * PI * Math.pow(radio, 3);

        System.out.println("Perimetro: " + perimetro);
        System.out.println("Area: " + area);
        System.out.println("Volumen: " + volumen);


    }   
}
