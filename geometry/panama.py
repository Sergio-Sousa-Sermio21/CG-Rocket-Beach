from geometry.geometry import Geometry
from core.obj_reader import *

class PanamaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
     
        
        # colors for faces in order:
        # x+, x-, y+, y-, z+, z-
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles
        position_data, uv_data, normal_data = my_obj_reader('panamabody.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
