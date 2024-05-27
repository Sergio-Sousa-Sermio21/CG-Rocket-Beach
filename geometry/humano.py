from geometry.geometry import Geometry
from core.obj_reader import *


class CalcaoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Calcoes.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class HumanoCorpoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Corpo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class HumanoDentesGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Dentes.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class HumanoLinguaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Lingua.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class HumanoCabeloGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/Cabelo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class HumanoOculosGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Humano/OculusMelhores.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)