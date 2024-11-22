 import math

def forma_triangulo (a, b, c): 
    return a + b > c and c > b and b + c > a
    def tipo_triangulo (a, b, c)
    if == b or b == c or a == c: 
    return "triangulo equilatero"
elif a == b or b == c or a == c: 
return "triangulo isóseceles"
else: 
return "triangulo escaleno"
def calculo_angulos (a, b, c): 
    
    print("Digite os comprimentos dos três lados do triângulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))


if forma_triangulo(lado1, lado2, lado3):
    print("Os lados formam um triângulo.")
    print("Tipo de triângulo:", tipo_triangulo(lado1, lado2, lado3))
    
    
    angulos = calcular_angulos(lado1, lado2, lado3)
    print("Ângulos do triângulo (em graus):")
    print(f"Ângulo A: {angulos[0]:.2f}°")
    print(f"Ângulo B: {angulos[1]:.2f}°")
    print(f"Ângulo C: {angulos[2]:.2f}°")
else:
    print("Os lados não podem formar um triângulo.")
