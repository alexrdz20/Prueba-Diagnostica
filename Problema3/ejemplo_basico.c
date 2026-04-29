#include <stdio.h>

int main() {
    int numero = 10;
    float pi = 3.1416;
    
    if (numero > 5) {
        printf("Es mayor\n");
    } else {
        printf("Es menor\n");
    }
    
    while (numero > 0) {
        numero--;
    }
    
    return 0;
}
