from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader


class BerlinMassaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        position_data, uv_data, normal_data = my_obj_reader('berlin_massa.obj')

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.count_vertices()
