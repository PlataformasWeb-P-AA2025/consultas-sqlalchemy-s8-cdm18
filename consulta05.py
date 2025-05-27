from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Tarea, Entrega, Curso

# Conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

cursos = session.query(Curso).join(Tarea).join(Entrega).all()

# for para recorrer todos los cursos
for curso in cursos:
    # el curso de iteacion
    print(f"Curso: {curso.titulo}")
    total_calificaciones = 0  # contador cal
    total_entregas = 0  # contador entregas

    # for para recorrer las tareas  del curso
    for tarea in curso.tareas:
        print(f"  Tarea: {tarea.titulo}")
        # Ciclo para recorrer las entregas realizadas en la tarea actual
        for entrega in tarea.entregas:
            # Muestra la calificación de cada entrega
            print(f"    Calificación de la entrega: {entrega.calificacion}")

            # Suma las calificaciones y cuenta las entregas
            total_calificaciones += entrega.calificacion
            total_entregas += 1

    if total_entregas > 0:
        # Si hay entregas, calcula el promedio
        promedio = total_calificaciones / total_entregas
        print(f"  Promedio de calificaciones para el curso '{curso.titulo}': {promedio:.2f}")
    else:
        # Si no hay entregas, muestra un mensaje informando que no hubo entregas
        print(f"  No hay entregas para el curso '{curso.titulo}'.")
