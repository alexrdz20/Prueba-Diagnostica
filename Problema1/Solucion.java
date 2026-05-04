import java.io.*;
import java.math.BigInteger;
import java.util.*;

/**
 * UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
 * Asignatura: Lenguajes y Compiladores
 * Problema 1: Polinomio (x+1)^n usando Triángulo de Pascal
 */
public class Solucion {
    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner sc = new Scanner(System.in);
        
        while (true) {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            System.out.println("\n==================================================");
            System.out.println("  EXPANSION POLINOMIAL (TRIANGULO DE PASCAL) - JAVA ");
            System.out.println("==================================================");
            System.out.println("  [1] Usar valores por defecto (n=100, x=2)");
            System.out.println("  [2] Ingresar valores manualmente");
            System.out.println("  [0] Salir");
            System.out.println("--------------------------------------------------");
            System.out.print("Seleccione una opcion > ");
            
            String op = sc.nextLine().trim();
            if (op.equals("0")) {
                System.out.println("Saliendo...");
                break;
            } else if (!op.equals("1") && !op.equals("2")) {
                System.out.println("[!] Opcion no valida.");
                continue;
            }

            int n = 100;
            int x = 2;

            if (op.equals("2")) {
                System.out.println("\n--- CONFIGURACION MANUAL ---");
                while (true) {
                    System.out.print("Ingrese el valor de n: ");
                    String input = sc.nextLine().trim();
                    try {
                        n = Integer.parseInt(input);
                        if (n >= 0) break;
                        System.out.println("Error: n debe ser >= 0.");
                    } catch (NumberFormatException e) {
                        System.out.println("Error: Ingrese un numero entero.");
                    }
                }
                while (true) {
                    System.out.print("Ingrese el valor de x: ");
                    String input = sc.nextLine().trim();
                    try {
                        x = Integer.parseInt(input);
                        break;
                    } catch (NumberFormatException e) {
                        System.out.println("Error: Ingrese un numero entero.");
                    }
                }
            }

            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            System.out.printf("\n[INFO] Calculando para n=%d, x=%d...\n", n, x);

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

            // 2. Calcular y guardar resultados
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
            System.out.printf("[OK] Completado en %.6f s. Revisa 'resultados_java.txt'\n", tiempo);
            System.out.print("\nPresione Enter para continuar...");
            sc.nextLine();
        }
    }
}
