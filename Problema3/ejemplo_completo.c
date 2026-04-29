#include <stdio.h>

/* 
   Este es un archivo de ejemplo largo para probar el traductor.
   Contiene comentarios de bloque, de linea, strings y muchas
   palabras reservadas de C.
*/

int calcular_suma(int limite) {
    int suma = 0;
    int i;
    
    // El traductor deberia cambiar 'for' por 'para'
    for (i = 1; i <= limite; i++) {
        suma += i;
    }
    
    return suma; // Deberia ser 'retornar'
}

void demostrar_switch(int opcion) {
    // Probando 'switch', 'case', 'default' y 'break'
    switch (opcion) {
        case 1:
            printf("Seleccionaste la opcion uno.\n");
            break;
        case 2:
            printf("Seleccionaste la opcion dos.\n");
            break;
        default:
            printf("Opcion no reconocida.\n");
    }
}

int main() {
    int contador = 0;
    float pi = 3.14159;
    double precision = 0.00001;
    char letra = 'A';
    
    printf("--- Inicio del programa de prueba ---\n");
    
    // Probando 'while' y 'if'/'else'
    while (contador < 5) {
        if (contador % 2 == 0) {
            printf("El numero %d es par\n", contador);
        } else {
            printf("El numero %d es impar\n", contador);
        }
        contador++;
    }
    
    int resultado = calcular_suma(10);
    printf("La suma de 1 a 10 es: %d\n", resultado);
    
    demostrar_switch(2);
    
    /*
      Nota: Las palabras dentro de este comentario NO deben traducirse.
      int, float, if, while, for, return.
    */
    
    printf("Mensaje con palabras reservadas: int float return (no deben cambiar)\n");
    
    return 0;
}
