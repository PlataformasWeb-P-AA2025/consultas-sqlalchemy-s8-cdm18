from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Departamento, Curso, Tarea, Entrega


# 2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3
# En función de los departamentos, presentar el nombre del departamento y el número de cursos que tiene cada departamento

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# se accede a cada clase necesaria para tener acceso a la siguiente que me va a dar el path hacia la que tiene lo que
# necesito, que seria (Entrega.calificacion)
departamentos_notas = session.query(Departamento).join(Curso).join(Tarea).join(Entrega).filter(Entrega.calificacion <= 0.3).all()
# for para recorrer los departamentos con notas menores o iguales a 0.3 y contarlos
for departamento in departamentos_notas:
    print(f"Departamento: {departamento.nombre}")
    print(f"Número de Cursos: {len(departamento.cursos)}")
    print("--------------------")  # separador

