import java.io.*;
/**
 * UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
 * Asignatura: Lenguajes y Compiladores
 * Problema 1: Polinomio (x+1)^n usando Triángulo de Pascal
 * 
 * Explicación:
 * El programa genera los coeficientes de un binomio elevado a la n utilizando
 * la lógica del Triángulo de Pascal. Se utiliza memoria dinámica (ArrayList)
 * y BigInteger para soportar n=100, ya que los coeficientes exceden el límite
 * de los tipos primitivos de Java.
 */
import java.math.BigInteger;
import java.util.*;

public class Solucion {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = 100;
        int x = 2;

        System.out.println("--- CONFIGURACION DEL POLINOMIO ---");
        
        // Entrada para n
        while (true) {
            System.out.print("Ingrese el valor de n (Enter para 100): ");
            String input = sc.nextLine().trim();
            if (input.isEmpty()) break;
            try {
                n = Integer.parseInt(input);
                if (n >= 0) break;
                System.out.println("Error: n debe ser un numero no negativo.");
            } catch (NumberFormatException e) {
                System.out.println("Error: Entrada invalida. Ingrese un numero entero.");
            }
        }

        // Entrada para x
        while (true) {
            System.out.print("Ingrese el valor de x para evaluar f(x) (Enter para 2): ");
            String input = sc.nextLine().trim();
            if (input.isEmpty()) break;
            try {
                x = Integer.parseInt(input);
                break;
            } catch (NumberFormatException e) {
                System.out.println("Error: Entrada invalida. Ingrese un numero entero.");
            }
        }

        // 1. Generar coeficientes (Fila de Pascal)
        long inicio = System.nanoTime();
        List<BigInteger> fila = new ArrayList<>();
        fila.add(BigInteger.ONE);
        for (int i = 0; i < n; i++) {
            List<BigInteger> nueva = new ArrayList<>();
            nueva.add(BigInteger.ONE);
            for (int j = 0; j < fila.size() - 1; j++) {
                nueva.add(fila.get(j).add(fila.get(j + 1)));
            }
            nueva.add(BigInteger.ONE);
            fila = nueva;
        }
        double tiempo = (System.nanoTime() - inicio) / 1e9;

        // 2. Formatear polinomio
        StringBuilder poli = new StringBuilder();
        for (int i = 0; i < fila.size(); i++) {
            int pot = n - i;
            BigInteger c = fila.get(i);
            if (!c.equals(BigInteger.ONE) || pot == 0) poli.append(c);
            if (pot > 0) poli.append("x").append(pot > 1 ? "^" + pot : "");
            if (i < fila.size() - 1) poli.append(" + ");
        }

        // 3. Calcular y guardar resultados
        try (PrintWriter out = new PrintWriter(new FileWriter("resultados_java.txt"))) {
            String line80 = "================================================================================";
            String lineSep = "--------------------------------------------------------------------------------";
            
            out.println(line80);
            out.println("           RESULTADOS DEL CALCULO POLINOMIAL (Problema 1)");
            out.println(line80);
            out.println("CONFIGURACION:");
            out.printf("  Grado (n) : %d\n", n);
            out.printf("  Valor (x) : %d\n", x);
            out.println(lineSep);
            out.printf("TIEMPO DE EJECUCION: %.6f segundos\n", tiempo);
            out.println(lineSep + "\n");

            BigInteger total = BigInteger.ZERO;
            BigInteger valX = BigInteger.valueOf(x);
            for (int i = 0; i < fila.size(); i++) {
                int pot = n - i;
                BigInteger c = fila.get(i);
                BigInteger termino = c.multiply(valX.pow(pot));
                total = total.add(termino);
            }

            out.println("RESULTADO FINAL:");
            out.println(total + "\n");
            out.println(line80);
        }
        System.out.println("Hecho. Revisa resultados_java.txt");
    }
}
