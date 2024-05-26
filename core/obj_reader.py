# credits: Margarida Moura, CGr 2022
#          Sergio Jesus, CG 2024 (modified)
#
"""Read vertices from OBJ file"""
from typing import List, Tuple, Type
from typing import List


def my_obj_reader(filename: str) -> List:
    """Get the vertices from the file"""
    position_list = list()
    vertices = list()

    with open(filename, 'r') as in_file:
        for line in in_file:
            if line[0] == 'v' and line[1] == ' ':
                point = [float(value) for value in line.strip().split()[1:]]
                vertices.append(point)
            elif line[0] == 'f' and line[1] == ' ':
                face_description = line.strip().split()[1:]
                for elem in face_description:
                    vertex_index = int(elem.split('/')[0]) - 1
                    position_list.append(vertices[vertex_index])

    return position_list


if __name__ == '__main__':
    f_in = input("File? ")
    result1 = my_obj_reader(f_in)
    print(result1)
