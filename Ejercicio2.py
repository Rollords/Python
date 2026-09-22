#Ejercicio 2 
#Registro de estudiantes y calificaciones
#Diseña un sistema donde se defina un diccionario para un curso. Primero solicita el nombre del curso y luego permite agregar los nombres de los alumnos en una lista. El ingreso de alumnos debe detenerse únicamente cuando el usuario presione la tecla "q". Al salir, imprime la lista completa en orden.

nombre_curso = input("Ingresa el nombre del curso: ")

curso = {
    "nombre": nombre_curso,
    "alumnos": [],
    "notas": []
}

print("\n--- Registro de Alumnos ---")
print("Ingresa los nombres de los alumnos (Escribe 'q' para finalizar):")

while True:
    nombre_alumno = input("Nombre del alumno: ").strip()
    
    if nombre_alumno.lower() == 'q':
        break
    
    if nombre_alumno:
        calificaciones= {
            'matematica' : '',
            'quimica' : '',
            'fisica' : '',
            'ingles' : '',
            'geografia' : ''
        }
        alumno_notas = []
        for materia in calificaciones:
            nota = int(input(f'¿Cuál fue la calificación de {nombre_alumno} en {materia}?: '))
            calificaciones[materia] = nota
            alumno_notas.append(nota)

        alumno_datos = {
            "nombre": nombre_alumno,
            "calificaciones": calificaciones
        }
        suma = sum(alumno_notas)
        total = suma / len(alumno_notas)
        curso["alumnos"].append(alumno_datos)
        curso["notas"].append(total)


print("\n" + "="*30)
print(f"Curso: {curso['nombre']}")
print(f"Total de alumnos registrados: {len(curso['alumnos'])}")
print("Lista de alumnos en orden alfabético:")
for i, alumno in enumerate(curso["alumnos"], start=1):
    print(f"{i}. {alumno}")
