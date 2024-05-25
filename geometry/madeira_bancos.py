from core.obj_reader import my_obj_reader
from geometry.geometry import Geometry
class MadeiraGeometry(Geometry):
    def __init__(self, width=3, height=1, depth=1):
        super().__init__()
        # vertices

        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-

        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles

        position_data, uv_data, normal_data = my_obj_reader('Madeira_Bancos.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", position_data)
        self.count_vertices()