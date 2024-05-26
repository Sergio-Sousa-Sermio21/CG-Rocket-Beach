from geometry.geometry import Geometry
from core.obj_reader import *


class CalcaoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Calcoes.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class HumanoCorpoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Corpo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class HumanoDentesGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Dentes.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class HumanoLinguaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Lingua.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class HumanoCabeloGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Cabelo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class HumanoOculosGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/oculos.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()