a,b,c = input().split()

a1 = float(a)
a2 = float(b)
a3 = float(c)

pi = 3.14159

area_triangulo = (a1*a3)/2
area_circulo = pi*(a3*a3)
area_trapezio = ((a1+a2)*a3)/2
area_quadrado = a2*a2
area_retangulo = a1*a2

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")