# credits: Margarida Moura, CGr 2022
#          Sergio Jesus, CG 2024 (modified)
#
"""Read vertices from OBJ file"""
from typing import List, Tuple, Type
from typing import List


def my_obj_reader(filename: str) -> Tuple[list[list[float]], list[list[float]], list[list[float]]]:
    """Get the vertices from the file"""
    position_list = list()
    uv_position_list = list()
    vn_position_list = list()
    vertices = list()
    uv_list = list()
    vn_list = list()

    with open(filename, 'r') as in_file:
        for line in in_file:
            if line[0] == 'v' and line[1] == ' ':
                point = [float(value) for value in line.strip().split()[1:]]
                vertices.append(point)
            elif line.startswith('vn '):
                vn = [float(value) for value in line.strip().split()[1:]]
                vn_list.append(vn)
            elif line.startswith('vt '):
                uv = [float(value) for value in line.strip().split()[1:]]
                uv_list.append(uv)
            elif line[0] == 'f' and line[1] == ' ':
                face_description = line.strip().split()[1:]
                for elem in face_description:
                    if len(elem.split('/')) == 1:
                        vertex_index = elem
                    else:
                        vertex_index, uv_index, vn_index = elem.split('/')
                        uv_index = int(uv_index) - 1
                        vn_index = int(vn_index) - 1
                        uv_position_list.append(uv_list[uv_index])
                        vn_position_list.append(vn_list[vn_index])
                    vertex_index = int(vertex_index) - 1
                    position_list.append(vertices[vertex_index])

    return position_list, 0, 0


if __name__ == '__main__':
    f_in = input("File? ")
    result1, result2, result3 = my_obj_reader(f_in)
    print(result1, result2, result3)
