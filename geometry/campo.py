from geometry.geometry import Geometry
from core.obj_reader import *


class BalizaAzulGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Baliza/ParteAzul.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class BalizaVermelhoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Baliza/ParteVermelho.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()

class BalizaBrancoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Baliza/ParteBranca.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class CampoTransparenteGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Estadio/ParteTransparente.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class CampoPartePretaGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Estadio/PartePreta.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class CampoParteAzulGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Estadio/ParteAzul.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()
