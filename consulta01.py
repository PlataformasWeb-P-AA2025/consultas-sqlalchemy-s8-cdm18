from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Departamento, Estudiante, Instructor, Entrega

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

entregas_arte = session.query(Entrega).filter(Departamento.nombre == 'Arte').all()
# for para recorrer las entregas de arte
for entregas in entregas_arte:
    print(f"Estudiante: {entregas.estudiante.nombre}")
    print(f"Tarea: {entregas.estudiante}")
    print(f"Calificación: {entregas.estudiante.entregas.calificacion}")
    print(f"Instructor: {entregas.curso.instructor}")
    print(f"Departamento: {entregas.estudiante.entregas.departamento}")
