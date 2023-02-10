# Programa para convertir una cantidad dada de grados centigrados a su equivalente en Farenheit y Kelvin

print("----------------------------------")
print("---- Conversor de Temperatura ----")
print("----------------------------------")

# input
C = int(input ("digite el valor de x: "))

# processing 
F = (C * 1.8 + 32)
K = ( C + 273.15)

# output 
print("----------------------------------")
print("---------- RESULTADOS ------------")
print("----------------------------------")
print("La converción de " + str(C) + " grados Celcius a Fahrenheit es " + str(F))
print("La converciòn de " + str(C) + " grados Celsius a Kelvin es " + str(K))