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
        int n = 100;
        int x = 2;

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
            out.printf("Resultados para n=%d, x=%d\n", n, x);
            out.printf("Tiempo de ejecucion: %.6f segundos\n\n", tiempo);
            out.println("Polinomio: " + poli.toString() + "\n");
            out.println("Calculo paso a paso:");

            BigInteger total = BigInteger.ZERO;
            BigInteger valX = BigInteger.valueOf(x);
            for (int i = 0; i < fila.size(); i++) {
                int pot = n - i;
                BigInteger c = fila.get(i);
                BigInteger termino = c.multiply(valX.pow(pot));
                total = total.add(termino);
                out.printf("%s*(%d^%d) = %s\n", c, x, pot, termino);
            }
            out.println("\nResultado final: " + total);
        }
        System.out.println("Hecho. Revisa resultados_java.txt");
    }
}
