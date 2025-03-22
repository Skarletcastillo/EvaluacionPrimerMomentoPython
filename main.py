estudiantes = {}

for i in range(3): 
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    estudiantes[nombre] = nota

promedio = sum(estudiantes.values()) / len(estudiantes)
print(f"El promedio de las notas es: {promedio:.2f}")

import openpyxl

libro = openpyxl.Workbook()

hoja = libro.active
hoja.title = "Ejercicio 5"

hoja['A1'] = "Nombre"
hoja['B1'] = "Nota"
hoja['B2'] = "Promedio"


fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila += 1

libro.save("ejercicio5.xlsx")
print("¡Ejercicio guardado en 'ejercicio5.xlsx'!")
