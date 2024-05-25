from geometry.geometry import Geometry
from core.obj_reader import *


class BalizaAzulGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles
        position_data, uv_data, normal_data = my_obj_reader('baliza_azulF2.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()


class BalizaChaoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data, uv_data, normal_data = my_obj_reader('baliza_chaoF.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()

class BalizaVermelhoGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        position_data, uv_data, normal_data = my_obj_reader('baliza_vermelhoF.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()

class CampoTransparenteGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('CampoParteTransparente.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()

class PartePretaGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('parte_preta_estadio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()

class RampaAzulGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('parte_rampa_azul_estadio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()

class RampaPretoGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('parte_rampa_preto2_estadio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()

class CampoTransparente2Geometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('parte_transparente2_estadio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()

class CampoChao2Geometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('parte_chao2_estadio.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()