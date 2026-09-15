#Ejercicio 2 
#Registro de estudiantes y calificaciones
#Diseña un sistema donde se defina un diccionario para un curso. Primero solicita el nombre del curso y luego permite agregar los nombres de los alumnos en una lista. El ingreso de alumnos debe detenerse únicamente cuando el usuario presione la tecla "q". Al salir, imprime la lista completa en orden.

curso = {}

#nombre del curso
nombre_curso = input("Ingresa el nombre del curso: ")
curso["nombre_curso"] = nombre_curso
curso["estudiantes"] = []

print("\nIngresa los nombres de los estudiantes (presiona 'q' para finalizar):")

while True:
    nombre = input("Nombre del estudiante: ").strip()
    
    if nombre.lower() == 'q':
        break
    
    if nombre:
        curso["estudiantes"].append(nombre)

curso["estudiantes"].sort()

print(f"\nCURSO: {curso['nombre_curso']}")
print("="*30)
print("Lista de estudiantes ordenada:")

for i, estudiante in enumerate(curso["estudiantes"], 1):
    print(f"{i}. {estudiante}")