from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import cadena_base_datos
from clases import Tarea, Entrega, Estudiante


# 2. Obtener todas las tareas asignadas a los siguientes estudiantes
#
# Jennifer Bolton
# Elaine Perez
# Heather Henderson
# Charles Harris
#
# En función de cada tarea, presentar el número de entregas que tiene

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

tareas_jennifer = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre == "Jennifer Bolton").all()
tareas_elaine = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre == "Elaine Perez").all()
tareas_heather = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre == "Heather Henderson").all()
tareas_charles = session.query(Tarea).join(Entrega).join(Estudiante).filter(Estudiante.nombre == "Charles Harris").all()

print(len(tareas_jennifer.entregas))
print(len(tareas_elaine.entregas))
print(len(tareas_heather.entregas))
print(len(tareas_charles.entregas))

