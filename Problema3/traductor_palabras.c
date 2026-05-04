#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { const char *eng, *esp; } PalabraReservada;

PalabraReservada dic[] = {
    {"auto", "automatico"}, {"break", "romper"}, {"case", "caso"}, {"char", "caracter"},
    {"const", "constante"}, {"continue", "continuar"}, {"default", "por_defecto"}, {"do", "hacer"},
    {"double", "doble"}, {"else", "sino"}, {"enum", "enumeracion"}, {"extern", "externo"},
    {"float", "flotante"}, {"for", "para"}, {"goto", "ir_a"}, {"if", "si"},
    {"int", "entero"}, {"long", "largo"}, {"register", "registro"}, {"return", "retornar"},
    {"short", "corto"}, {"signed", "con_signo"}, {"sizeof", "tamano_de"}, {"static", "estatico"},
    {"struct", "estructura"}, {"switch", "segun"}, {"typedef", "definir_tipo"}, {"union", "union"},
    {"unsigned", "sin_signo"}, {"void", "vacio"}, {"volatile", "volatil"}, {"while", "mientras"}
};

int total_pal = sizeof(dic) / sizeof(dic[0]);

const char *traducir(const char *palabra) {
    for (int i = 0; i < total_pal; i++) {
        if (strcmp(palabra, dic[i].eng) == 0) return dic[i].esp;
    }
    return palabra;
}

void procesar_archivo(const char *nombre) {
    FILE *archivo = fopen(nombre, "r");
    if (!archivo) {
        printf("\n[ERROR] No se pudo abrir '%s'.\n", nombre);
        return;
    }

    /* Obtener tamaño del archivo para la memoria dinamica */
    fseek(archivo, 0, SEEK_END);
    long tamano = ftell(archivo);
    fseek(archivo, 0, SEEK_SET);

    /* Cargar en memoria de forma dinamica (Cumple requisito del PDF) */
    char *codigo = (char *)malloc(tamano + 1);
    if (!codigo) {
        printf("\n[ERROR] No se pudo reservar memoria.\n");
        fclose(archivo);
        return;
    }

    fread(codigo, 1, tamano, archivo);
    codigo[tamano] = '\0';
    fclose(archivo);

    system("cls"); /* Limpia pantalla de traduccion */
    printf("\n[OK] Cargando archivo en memoria: %s\n", nombre);
    printf("--------------------------------------------------\n");
    printf("   CODIGO TRADUCIDO AL ESPANOL:\n");
    printf("--------------------------------------------------\n\n");

    char temp[256];
    int j = 0, str = 0, c_lin = 0, c_blq = 0;

    for (long i = 0; i <= tamano; i++) {
        int c = codigo[i];
        int ant = i > 0 ? codigo[i - 1] : 0;
        int sig = i < tamano ? codigo[i + 1] : '\0';

        if (!c_lin && !c_blq && !str) {
            if (c == '/' && sig == '/') c_lin = 1;
            else if (c == '/' && sig == '*') c_blq = 1;
            else if (c == '\"') str = 1;
        } else if (c_lin && c == '\n') {
            c_lin = 0;
        } else if (c_blq && c == '*' && sig == '/') {
            putchar(c); putchar(sig);
            c_blq = 0; i++; continue;
        } else if (str && c == '\"' && ant != '\\') {
            str = 0;
        }

        if (str || c_lin || c_blq) {
            if (j > 0) { temp[j] = '\0'; printf("%s", traducir(temp)); j = 0; }
            if (c != '\0') putchar(c);
        } else if (isalnum(c) || c == '_') {
            if (j < 255) temp[j++] = c;
        } else {
            if (j > 0) { temp[j] = '\0'; printf("%s", traducir(temp)); j = 0; }
            if (c != '\0') putchar(c);
        }
    }

    free(codigo); /* Liberar memoria */
    
    printf("\n\n--------------------------------------------------\n");
    printf("   [INFO] COMPLETADO EXITOSAMENTE\n");
    printf("--------------------------------------------------\n");
}

int main(int argc, char *argv[]) {
    if (argc >= 2) {
        procesar_archivo(argv[1]);
        return 0;
    }

    char in[256], nom[256];
    while (1) {
        system("cls"); /* Limpia pantalla del menu */
        printf("\n==================================================\n");
        printf("       TRADUCTOR DE CODIGO C A ESPANOL            \n");
        printf("==================================================\n");
        printf("  [1] Ingresar nombre de archivo manualmente      \n");
        printf("  [2] Usar Ejemplo basico (ejemplo_basico.c)      \n");
        printf("  [3] Usar Ejemplo completo (ejemplo_completo.c)  \n");
        printf("  [0] Salir                                       \n");
        printf("--------------------------------------------------\n> ");

        if (!fgets(in, sizeof(in), stdin)) break;
        in[strcspn(in, "\n")] = 0;

        if (strcmp(in, "0") == 0) break;
        else if (strcmp(in, "1") == 0) {
            printf(">> Archivo: ");
            if (fgets(in, sizeof(in), stdin)) {
                in[strcspn(in, "\n")] = 0;
                strcpy(nom, in);
            } else continue;
        } 
        else if (strcmp(in, "2") == 0) strcpy(nom, "ejemplo_basico.c");
        else if (strcmp(in, "3") == 0) strcpy(nom, "ejemplo_completo.c");
        else continue;

        procesar_archivo(nom);
        printf("\nEnter para continuar...");
        fgets(in, sizeof(in), stdin);
    }
    return 0;
}
