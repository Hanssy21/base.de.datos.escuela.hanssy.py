#escuela = {}: Crea un diccionario llamado escuela, que representará nuestra "base de datos".
#'estudiantes': []: Dentro del diccionario escuela, creamos una clave llamada 'estudiantes' que almacena una lista de diccionarios. 
# Cada diccionario dentro de la lista representa a un estudiante.
#Cada diccionario de estudiante tiene claves como
#  nombre, edad, curso y nota, que contienen los valores correspondientes de cada estudiante.
escuela = {
    'estudiantes': [
        {'nombre': 'Ana', 'edad': 20, 'curso': 'Matemáticas', 'nota': 9.2},                                      
        {'nombre': 'Luis', 'edad': 21, 'curso': 'Historia', 'nota': 8.5}, 
        {'nombre': 'Pedro', 'edad': 22, 'curso': 'Física', 'nota': 7.8},              
        {'nombre': 'Maria', 'edad': 19, 'curso': 'Biología', 'nota': 6.3},
        {'nombre': 'Juan', 'edad': 20, 'curso': 'Química', 'nota': 8.9}
    ]
}
# Encontrar estudiantes con nota mayor a 8
def estudiantes_con_nota_mayor_a_8():
    resultado = [estudiante for estudiante in escuela['estudiantes'] if estudiante['nota'] > 8]
    return resultado

# Encontrar estudiantes con 20 años
def estudiantes_con_20_anos():
    resultado = [estudiante for estudiante in escuela['estudiantes'] if estudiante['edad'] == 20]
    return resultado

# Actualizar la nota de un estudiante
def actualizar_nota(nombre, nueva_nota):
    for estudiante in escuela['estudiantes']:
        if estudiante['nombre'] == nombre:
            estudiante['nota'] = nueva_nota
            return f"Nota de {nombre} actualizada a {nueva_nota}."
    return f"Estudiante {nombre} no encontrado."

# Incrementar la edad de todos los estudiantes en 1 año
def incrementar_edad():
    for estudiante in escuela['estudiantes']:
        estudiante['edad'] += 1
    return "Edad de todos los estudiantes incrementada en 1 año."

# Encontrar estudiantes con una nota entre 7 y 9 y con menos de 22 años
def estudiantes_nota_entre_7_y_9_y_menores_de_22():
    resultado = [estudiante for estudiante in escuela['estudiantes'] 
                 if 7 <= estudiante['nota'] <= 9 and estudiante['edad'] < 22]
    return resultado

# Calcular el promedio de las notas
def calcular_promedio_notas():
    total_notas = sum(estudiante['nota'] for estudiante in escuela['estudiantes'])
    promedio = total_notas / len(escuela['estudiantes'])
    return promedio

# Agrupar estudiantes por curso y calcular la nota promedio por curso
def promedio_por_curso():
    cursos = {}
    for estudiante in escuela['estudiantes']:
        curso = estudiante['curso']
        if curso not in cursos:
            cursos[curso] = {'total_notas': 0, 'cantidad': 0}
        cursos[curso]['total_notas'] += estudiante['nota']
        cursos[curso]['cantidad'] += 1
    
    for curso, datos in cursos.items():
        promedio = datos['total_notas'] / datos['cantidad']
        print(f"Promedio de notas en {curso}: {promedio:.2f}")

# Llamadas a las funciones para ver los resultados

if __name__ == "__main__":
    # Estudiantes con nota mayor a 8
    print("Estudiantes con nota mayor a 8:")
    estudiantes_mayores_a_8 = estudiantes_con_nota_mayor_a_8()
    for estudiante in estudiantes_mayores_a_8:
        print(estudiante)
    
    # Estudiantes con 20 años
    print("\nEstudiantes con 20 años:")
    estudiantes_20_anos = estudiantes_con_20_anos()
    for estudiante in estudiantes_20_anos:
        print(estudiante)

    # Actualizar la nota de Ana
    print("\nActualizando la nota de Ana...")
    print(actualizar_nota('Ana', 9.5))

    # Incrementar la edad de todos los estudiantes
    print("\nIncrementando la edad de todos los estudiantes...")
    print(incrementar_edad())

    # Estudiantes con nota entre 7 y 9 y menos de 22 años
    print("\nEstudiantes con nota entre 7 y 9 y menos de 22 años:")
    estudiantes_filtrados = estudiantes_nota_entre_7_y_9_y_menores_de_22()
    for estudiante in estudiantes_filtrados:
        print(estudiante)

    # Calcular el promedio de las notas
    print(f"\nPromedio de notas: {calcular_promedio_notas():.2f}")

    # Promedio de notas por curso
    print("\nPromedio de notas por curso:")
    promedio_por_curso()