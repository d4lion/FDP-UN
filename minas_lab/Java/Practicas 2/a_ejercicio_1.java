import java.util.Scanner;


public class a_ejercicio_1 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int numero = Integer.parseInt(scanner.next());

        scanner.close();

        if (numero % 5 == 0){
            System.out.format("El numero %d es multiplo de 5", numero);
        }else{
            System.out.format("El numero %d no es multiplo de 5", numero);
        }
    }
}
