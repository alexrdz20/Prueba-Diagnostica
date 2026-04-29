/**
 * UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
 * Asignatura: Lenguajes y Compiladores
 * Problema 3: Traductor de Palabras Reservadas en C
 * 
 * Explicación:
 * Carga un archivo .c dinámicamente en memoria usando malloc.
 * Escanea el contenido ignorando comentarios y strings para traducir
 * únicamente las palabras reservadas a su equivalente en español.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Estructura para mapear palabras reservadas */
typedef struct {
    const char *eng;
    const char *esp;
} PalabraReservada;

/* Tabla de traduccion de palabras reservadas en C */
PalabraReservada diccionario[] = {
    {"auto", "automatico"}, {"break", "romper"}, {"case", "caso"},
    {"char", "caracter"}, {"const", "constante"}, {"continue", "continuar"},
    {"default", "por_defecto"}, {"do", "hacer"}, {"double", "doble"},
    {"else", "sino"}, {"enum", "enumeracion"}, {"extern", "externo"},
    {"float", "flotante"}, {"for", "para"}, {"goto", "ir_a"},
    {"if", "si"}, {"int", "entero"}, {"long", "largo"},
    {"register", "registro"}, {"return", "retornar"}, {"short", "corto"},
    {"signed", "con_signo"}, {"sizeof", "tamano_de"}, {"static", "estatico"},
    {"struct", "estructura"}, {"switch", "segun"}, {"typedef", "definir_tipo"},
    {"union", "union"}, {"unsigned", "sin_signo"}, {"void", "vacio"},
    {"volatile", "volatil"}, {"while", "mientras"}
};

int total_palabras = sizeof(diccionario) / sizeof(diccionario[0]);

/* Funcion para buscar la traduccion de una palabra */
const char* buscar_traduccion(const char *palabra) {
    int i;
    for (i = 0; i < total_palabras; i++) {
        if (strcmp(palabra, diccionario[i].eng) == 0) {
            return diccionario[i].esp;
        }
    }
    return palabra; /* Si no es reservada, devuelve la misma palabra */
}

int main(int argc, char *argv[]) {
    FILE *archivo;
    long tamano;
    char *codigo;
    char temporal[256];
    int i, j = 0;
    int en_string = 0;
    int en_comentario_linea = 0;
    int en_comentario_bloque = 0;

    if (argc < 2) {
        printf("Error: Debes proporcionar el nombre del archivo.\n");
        printf("Uso: %s ejemplo_basico.c\n", argv[0]);
        return 1;
    }

    /* Abrir el archivo */
    archivo = fopen(argv[1], "rb");
    if (!archivo) {
        perror("Error al abrir el archivo");
        return 1;
    }

    /* Obtener el tamano del archivo */
    fseek(archivo, 0, SEEK_END);
    tamano = ftell(archivo);
    if (tamano < 0) {
        perror("Error al obtener el tamano del archivo");
        fclose(archivo);
        return 1;
    }
    fseek(archivo, 0, SEEK_SET);

    /* Reservar memoria dinamicamente */
    codigo = (char *)malloc(tamano + 1);
    if (!codigo) {
        printf("Error: No se pudo reservar memoria.\n");
        fclose(archivo);
        return 1;
    }

    /* Leer el archivo a la memoria */
    if (fread(codigo, 1, tamano, archivo) < (size_t)tamano && ferror(archivo)) {
        printf("Error al leer el archivo.\n");
        free(codigo);
        fclose(archivo);
        return 1;
    }
    codigo[tamano] = '\0';
    fclose(archivo);

    printf("--- PROCESANDO ARCHIVO: %s ---\n", argv[1]);
    printf("--- CODIGO TRADUCIDO AL ESPANOL ---\n\n");

    /* Procesar el codigo caracter por caracter */
    for (i = 0; i <= tamano; i++) {
        char c = codigo[i];
        char prox = (i + 1 < tamano) ? codigo[i+1] : '\0';

        /* Manejo de comentarios y strings */
        if (!en_comentario_linea && !en_comentario_bloque && !en_string) {
            if (c == '/' && prox == '/') {
                en_comentario_linea = 1;
            } else if (c == '/' && prox == '*') {
                en_comentario_bloque = 1;
            } else if (c == '\"') {
                en_string = 1;
            }
        } else if (en_comentario_linea && c == '\n') {
            en_comentario_linea = 0;
        } else if (en_comentario_bloque && c == '*' && prox == '/') {
            /* Imprimir el '*' y el '/' y avanzar el indice */
            putchar(c);
            i++;
            putchar(codigo[i]);
            en_comentario_bloque = 0;
            continue;
        } else if (en_string && c == '\"' && (i == 0 || codigo[i-1] != '\\')) {
            en_string = 0;
        }

        /* Si estamos en un estado que no permite traduccion (string o comentario) */
        if (en_string || en_comentario_linea || en_comentario_bloque) {
            if (j > 0) { /* Por si acaso habia una palabra antes */
                temporal[j] = '\0';
                printf("%s", buscar_traduccion(temporal));
                j = 0;
            }
            if (c != '\0') putchar(c);
            continue;
        }

        /* Si es una letra o numero (identificador) */
        if (isalnum(c) || c == '_') {
            if (j < 255) {
                temporal[j++] = c;
            }
        } else {
            /* Si teniamos una palabra acumulada, la traducimos */
            if (j > 0) {
                temporal[j] = '\0';
                printf("%s", buscar_traduccion(temporal));
                j = 0;
            }
            /* Imprimir el caracter no alfanumerico */
            if (c != '\0') {
                putchar(c);
            }
        }
    }

    printf("\n\n--- FIN DE LA TRADUCCION ---\n");

    /* Liberar memoria dinamica */
    free(codigo);

    return 0;
}
