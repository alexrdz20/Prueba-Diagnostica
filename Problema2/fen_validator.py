"""
UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA - Lenguajes y Compiladores
Problema 2: Validador y Analizador FEN (Versión Final Robusta)
"""
import re
import os

def analizar_fen(fen):
    partes = fen.strip().split()
    if len(partes) != 6:
        return False, "Error: La cadena debe tener exactamente 6 campos."

    tablero, turno, enroque, paso, medio, total = partes

    # 1. Validar Filas y Piezas (Strict)
    filas = tablero.split('/')
    if len(filas) != 8:
        return False, "Error: El tablero debe tener 8 filas."
    
    for fila in filas:
        n = 0
        for c in fila:
            if c.isdigit():
                if c == '0': return False, "Error: El dígito '0' no es válido."
                n += int(c)
            elif c.lower() in 'pnbrqk':
                n += 1
            else:
                return False, f"Error: Carácter inválido '{c}' en el tablero."
        if n != 8:
            return False, f"Error: Fila con longitud inválida ({n} en lugar de 8)."

    # 2. Validar Turno y Enroque
    if turno not in ['w', 'b']:
        return False, "Error: Turno inválido (debe ser 'w' o 'b')."
    
    if enroque != '-' and not re.fullmatch(r'[KQkq]+', enroque):
        return False, "Error: Formato de enroque inválido."

    # 3. Validar Peón al paso y Contadores
    if (paso != '-' and not re.fullmatch(r'[a-h][36]', paso)):
        return False, "Error: Coordenada de peón al paso inválida."
    
    if not medio.isdigit() or not total.isdigit():
        return False, "Error: Los contadores de jugadas deben ser números."

    # 4. Construcción de la descripción (Si es válida)
    m = {'K':'Blanco(R)', 'Q':'Blanco(D)', 'k':'Negro(R)', 'q':'Negro(D)'}
    enroques = [m[c] for c in enroque if c in m]
    
    analisis = [
        f"Turno        : {'Blancas' if turno == 'w' else 'Negras'}",
        f"Enroques     : {', '.join(enroques) if enroques else 'Ninguno'}",
        f"Peón al paso : {paso if paso != '-' else 'No hay'}",
        f"Jugada nro   : {total} (Reloj 50 mov: {medio})"
    ]
    return True, "\n".join(analisis)

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("="*45)
        print("   ANALIZADOR FEN (AJEDREZ)")
        print("="*45)
        print("\n1. Cargar ejemplo | 2. Entrada manual | 0. Salir")
        op = input("> ").strip()
        if op == "0": break
        
        cadena = ""
        if op == "1":
            try:
                from datos_fen import FEN_EJEMPLO
                cadena = FEN_EJEMPLO
                print(f"\n[INFO] Procesando: {cadena}")
            except:
                print("\n[!] Error: No se encontró datos_fen.py")
        elif op == "2":
            cadena = input("\nIngrese FEN: ").strip()
        
        if cadena:
            os.system('cls' if os.name == 'nt' else 'clear')
            valido, resultado = analizar_fen(cadena)
            print(f"\n[{'V' if valido else 'X'}] {'CADENA VÁLIDA' if valido else 'CADENA INVÁLIDA'}")
            print(f"{'-' * 45}\n{resultado}\n{'-' * 45}")
            input("\nPresione Enter para continuar...")
