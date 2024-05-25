# credits: Margarida Moura, CGr 2022
#          Sergio Jesus, CG 2024 (modified)
#
"""Read vertices from OBJ file"""
from typing import List, Tuple, Type


def my_obj_reader(filename: str):
    """Get the vertices from the file"""
    position_list = list()
    vertices = list()
    vn = list()
    vt = list()

    with open(filename, 'r') as in_file:
        for line in in_file:
            if line[0] == 'v':
                if line[1] == 't':
                    point = [float(value) for value in line.strip().split()[1:]]
                    vt.append(point)
                elif line[1] == 'n':
                    point = [float(value) for value in line.strip().split()[1:]]
                    vn.append(point)
                else:
                    point = [float(value) for value in line.strip().split()[1:]]
                    vertices.append(point)
            elif line[0] == 'f':
                face_description = [int(value) - 1 for value in line.strip().split()[1:]]
                for elem in face_description:
                    position_list.append(vertices[elem])
    return position_list,0,0


if __name__ == '__main__':
    f_in = input("File? ")
    result, result2, result3 = my_obj_reader(f_in)
    print(result, result2, result3)
