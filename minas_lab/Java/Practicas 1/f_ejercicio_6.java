import java.util.Scanner;

public class f_ejercicio_6 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        double Fah = scanner.nextDouble();

        scanner.close();
    
        double resultado = (5.0/9.0) * (Fah - 32);
        
        System.out.println(resultado);

    }

}
