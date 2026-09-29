#Ejercicio 2 
#Registro de estudiantes y calificaciones
#Diseña un sistema donde se defina un diccionario para un curso. Primero solicita el nombre del curso y luego permite agregar los nombres de los alumnos en una lista. El ingreso de alumnos debe detenerse únicamente cuando el usuario presione la tecla "q". Al salir, imprime la lista completa en orden.

nombre_curso = input("Ingresa el nombre del curso: ")

curso = {
    "nombre": nombre_curso,
    "alumnos": []
}

print("\n--- Registro de Alumnos ---")
print("Ingresa los nombres de los alumnos (Escribe 'q' para finalizar):")

while True:
    nombre_alumno = input("Nombre del alumno: ").strip()
    
    if nombre_alumno.lower() == 'q':
        break
    
    if nombre_alumno:
        materias= ['Matematica','Quimica','Fisica','Ingles']
        calificaciones = {}

        for materia in materias:
            nota = int(input(f'¿Cuál fue la calificación de {nombre_alumno} en {materia}?: '))
            calificaciones[materia] = nota

            total_notas = sum(calificaciones.values()) / len(calificaciones)

        alumno_datos = {
            "Nombre": nombre_alumno,
            "Calificaciones": calificaciones,
            "Promedio" : total_notas
        }

        
        curso["alumnos"].append(alumno_datos)


print("\n" + "="*30)
print(f"Curso: {curso['nombre']}")
print(f"Total de alumnos registrados: {len(curso['alumnos'])}")
print("Lista de alumnos en orden alfabético:")
for i, alumno in enumerate(curso["alumnos"], start=1):
    print(f"{i}. {alumno}")
