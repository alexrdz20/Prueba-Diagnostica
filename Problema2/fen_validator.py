"""
UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
Asignatura: Lenguajes y Compiladores
Problema 2: Validador de Notación FEN (Forsyth-Edwards Notation)

Explicación:
Valida si una cadena cumple con el estándar FEN, verificando:
1. Las 8 filas del tablero.
2. El turno (w/b).
3. Disponibilidad de enroque.
4. Peón al paso.
5. Regla de los 50 movimientos.
6. Número de jugada completa.
"""
import re

def validate_fen(fen):
    """
    Valida si una cadena C se encuentra en notación FEN (Forsyth-Edwards Notation).
    Retorna True si es válida, False en caso contrario.
    """
    # 1. Verificar que tenga 6 campos separados por espacios
    fields = fen.strip().split(' ')
    if len(fields) != 6:
        return False

    placement, color, castling, en_passant, halfmove, fullmove = fields

    # 2. Validar Piece Placement (Campo 1)
    ranks = placement.split('/')
    if len(ranks) != 8:
        return False
    
    for rank in ranks:
        squares = 0
        for char in rank:
            if char.isdigit():
                # Si es dígito, debe ser entre 1 y 8
                if char == '0': return False
                squares += int(char)
            elif char.lower() in 'pnbrqk':
                # Si es pieza, suma 1 cuadrado
                squares += 1
            else:
                # Carácter no permitido
                return False
        if squares != 8:
            return False

    # 3. Validar Active Color (Campo 2)
    if color not in ['w', 'b']:
        return False

    # 4. Validar Castling Availability (Campo 3)
    if castling != '-':
        if not re.fullmatch(r'[KQkq]+', castling) or len(set(castling)) != len(castling):
            return False

    # 5. Validar En Passant Target Square (Campo 4)
    if en_passant != '-':
        # Debe ser una coordenada válida (ej. e3, a6)
        if not re.fullmatch(r'[a-h][36]', en_passant):
            return False

    # 6. Validar Halfmove Clock (Campo 5)
    if not halfmove.isdigit():
        return False

    # 7. Validar Fullmove Number (Campo 6)
    if not fullmove.isdigit() or int(fullmove) <= 0:
        return False

    return True

# Ejemplos de uso:
if __name__ == "__main__":
    print("--- VALIDADOR DE NOTACIÓN FEN ---")
    
    while True:
        print("\nSeleccione cómo ingresar la cadena FEN:")
        print("1. Importar desde archivo de código (datos_fen.py)")
        print("2. Ingresar manualmente por teclado")
        print("0. Salir")
        
        opcion = input("> ").strip()
        
        if opcion == "0" or opcion.lower() == "salir":
            break
            
        c = ""
        if opcion == "1":
            try:
                # Importar dinámicamente el archivo de datos
                from datos_fen import FEN_EJEMPLO
                c = FEN_EJEMPLO
                print(f"Cadena importada correctamente: {c}")
            except ImportError:
                print("Error: No se encontró el archivo 'datos_fen.py'.")
                continue
            except Exception as e:
                print(f"Error al importar los datos: {e}")
                continue
                
        elif opcion == "2":
            c = input("Ingrese la cadena FEN: ").strip()
        else:
            print("Opción no válida.")
            continue
        
        if not c:
            print("Error: No se proporcionó ninguna cadena FEN.")
            continue

        if validate_fen(c):
            print(">>> RESULTADO: La cadena FEN es VÁLIDA.")
        else:
            print(">>> RESULTADO: La cadena FEN es INVÁLIDA.")
