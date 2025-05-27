from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Curso, Tarea, Instructor, Entrega, Departamento

# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte.
# En función de la entrega, presentar:
# nombre de la tarea, nombre del estudiante, calificación, nombre de instructor y nombre del departamento
# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas_arte = session.query(Entrega).join(Tarea).join(Curso).join(Departamento).join(Instructor).filter(Departamento.nombre == 'Arte').all()

# for para recorrer las entregas de arte
for entregas in entregas_arte:
    print(f"Estudiante: {entregas.estudiante.nombre}")
    print(f"Tarea: {entregas.estudiante.inscripciones.curso}")
