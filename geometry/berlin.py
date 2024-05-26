from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


#Falta o objeto da bola de berlin grande
class BerlinExplosaoMassaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        position_data = my_obj_reader('berlin_massa.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


#Falta o objeto da bola de berlin grande
class BerlinExplosaoRecheioGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        position_data = my_obj_reader('berlin_recheio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BerlinComerMassaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        position_data = my_obj_reader('Objetos/Modelos/Humano/Bola.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BerlinComerRecheioGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        position_data = my_obj_reader('Objetos/Modelos/Humano/Icing.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()