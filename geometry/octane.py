from geometry.geometry import Geometry
from core.obj_reader import *


class OctaneCarcacaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/ParteVermelha.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class OctaneMotorGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/Motor.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)

class OctaneJanelaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/Janelas.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)

class OctaneLinhasGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/LinhasPretas.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)

class RodasFrenteGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/RodasFrente/rodasFrente.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)

class RodasTrasGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/RodasAtras/rodasAtras.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class PanamaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/panama.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)


class PanamaFitaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Octane/Fita.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.add_attribute("vec3", "vertexNormal", position_data)
        self.add_attribute("vec3", "faceNormal", position_data)