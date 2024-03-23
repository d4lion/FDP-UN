import java.util.Scanner;

class b_ejercicio_2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String nombre = scanner.nextLine();
        int numeroEntero = Integer.parseInt(scanner.next());
        float numeroFlotante = Float.parseFloat(scanner.next());
        
        scanner.close();

        System.out.println("Mi nombre es: " + nombre);
        System.out.println("Mi entero es: " + numeroEntero);
        System.out.println("Mi flotante es: " + numeroFlotante);

    }
}