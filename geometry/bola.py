from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class BolaParteAmarela(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bola/ParteAmarelo.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BolaParteAzul(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bola/ParteAzul.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BolaParteBranca(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bola/ParteBranco.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BolaParteVerde(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bola/ParteVerde.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()


class BolaParteVermelha(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()

        position_data = my_obj_reader('Objetos/Modelos/Bola/ParteVermelha.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()