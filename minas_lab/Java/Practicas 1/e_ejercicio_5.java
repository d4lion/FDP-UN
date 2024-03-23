import java.util.Scanner;

public class e_ejercicio_5 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        float valor = Float.parseFloat(scanner.next());        
        scanner.close();

        double valorIva = valor * 0.19;
        double valorPropina = valor * 0.10;

        double valorTotal = valor + valorIva + valorPropina;

        System.out.println("Total consumido: COP$ " + valor);
        System.out.println("Valor IVA: COP$ " + valorIva);
        System.out.println("Valor propina: COP$ " + valorPropina);
        System.out.println("A pagar: COP$ " + valorTotal);
    }
}
