from geometry.geometry import Geometry
from geometry.ellipsoid import EllipsoidGeometry
from core.obj_reader import my_obj_reader

class parteBranca(Geometry):
    def __init__(self, radius=1, radius_segments=32, height_segments=16):
        super().__init__()
        # colors for faces in order:
        c1, c2 = [1, 0.5, 0.5], [0.5, 0, 0]
        c3, c4 = [0.5, 1, 0.5], [0, 0.5, 0]
        c5, c6 = [0.5, 0.5, 1], [0, 0, 0.5]
        # x+, x-, y+, y-, z+, z-
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        # Each side consists of two triangles
        position_data, uv_data, normal_data = my_obj_reader('ParteBranca.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()
