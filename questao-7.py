import math

def eh_triangulo(a, b, c):
    """Verifica se os lados a, b e c podem formar um triângulo."""
    return a + b > c and a + c > b and b + c > a

def calcular_angulos(a, b, c):
    """Calcula os ângulos do triângulo em graus usando a lei dos cossenos."""
    angulo_A = math.degrees(math.acos(max(-1, min(1, (b**2 + c**2 - a**2) / (2 * b * c)))))
    angulo_B = math.degrees(math.acos(max(-1, min(1, (a**2 + c**2 - b**2) / (2 * a * c)))))
    angulo_C = 180 - angulo_A - angulo_B
    return [angulo_A, angulo_B, angulo_C]

def classificar_triangulo(a, b, c, angulos):
    """Classifica o triângulo quanto aos lados e aos ângulos."""
    # Classificação quanto aos lados
    if a == b == c:
        tipo_lados = "Equilátero"
    elif a == b or b == c or a == c:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"
    
    # Classificação quanto aos ângulos
    maior_angulo = max(angulos)
    if maior_angulo == 90:
        tipo_angulos = "Retângulo"
    elif maior_angulo > 90:
        tipo_angulos = "Obtuso"
    else:
        tipo_angulos = "Agudo"
    
    return tipo_lados, tipo_angulos

def validar_entrada(valor):
    """Valida se a entrada é um número positivo."""
    try:
        numero = float(valor)
        return numero if numero > 0 else None
    except ValueError:
        return None

def main():
    print("Verificador de Triângulos")
    
    # Entrada validada pelo usuário
    lados = []
    for i in ['a', 'b', 'c']:
        while True:
            entrada = input(f"Digite o comprimento do lado {i}: ")
            lado = validar_entrada(entrada)
            if lado is not None:
                lados.append(lado)
                break
            print("Por favor, insira um número positivo válido.")
    
    a, b, c = lados

    if not eh_triangulo(a, b, c):
        print("Os comprimentos fornecidos não podem formar um triângulo.")
        return
    
    angulos = calcular_angulos(a, b, c)
    tipo_lados, tipo_angulos = classificar_triangulo(a, b, c, angulos)
    
    print(f"\nÂngulos do triângulo: {angulos[0]:.2f}°, {angulos[1]:.2f}°, {angulos[2]:.2f}°")
    print(f"Classificação quanto aos lados: {tipo_lados}")
    print(f"Classificação quanto aos ângulos: {tipo_angulos}")

if __name__ == "__main__":
    main()
