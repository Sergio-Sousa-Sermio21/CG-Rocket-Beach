from core.obj_reader import my_obj_reader
from geometry.geometry import Geometry


class MadeiraGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bancos/Madeira/Madeira.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class TubosGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bancos/Tubos/Tubos.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)