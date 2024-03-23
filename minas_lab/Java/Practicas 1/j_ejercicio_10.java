import java.util.Scanner;

public class j_ejercicio_10 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String cadena = scan.next();
        scan.close();

        String[] cadenaNumeros = cadena.split("");
        
        int resultadoSuma = 0;

        for (String numero: cadenaNumeros){
            resultadoSuma += Integer.parseInt(numero);
        }

        System.out.format("%s + %s + %s = %d", cadenaNumeros[0], cadenaNumeros[1], cadenaNumeros[2], resultadoSuma);

    }
}
