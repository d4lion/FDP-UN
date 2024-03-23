import java.util.Scanner;

public class c_ejercicio_3 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String edad = scanner.next();
        String nombre = scanner.next();
        String peso = scanner.next();

        scanner.close();

        String mensaje = String.format("Tengo %s, me llamo %s y peso %s", edad, nombre, peso);
    
        System.out.println(mensaje);
    }
}
