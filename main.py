import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr


class Cube:
    def __init__(self, position, eulers):
        self.position = np.array(position, dtype=np.float32)
        self.eulers = np.array(eulers, dtype=np.float32)


class CubeMesh:

    def __init__(self):
        #Temos de organizar os vertices ao contrário do sentido dos ponteiros do relógio
        #x, y, z, s, t
        self.vertices = (
            # Face 1 Triangulo 1
            -0.5, -0.5, -0.5, 0, 0,     #vertix 1
             0.5, -0.5, -0.5, 1, 0,     #vertix 2
             0.5,  0.5, -0.5, 1, 1,     #vertix 3

            # Face 1 Triangulo 2
             0.5,  0.5, -0.5, 1, 1,     #vertix 1
            -0.5,  0.5, -0.5, 0, 1,     #vertix 2
            -0.5, -0.5, -0.5, 0, 0,     #vertix 3

            # Face 2 Triangulo 1
            -0.5, -0.5,  0.5, 0, 0,     #vertix 1
             0.5, -0.5,  0.5, 1, 0,     #vertix 2
             0.5,  0.5,  0.5, 1, 1,     #vertix 3

            # Face 2 Triangulo 2
             0.5,  0.5,  0.5, 1, 1,     #vertix 1
            -0.5,  0.5,  0.5, 0, 1,     #vertix 2
            -0.5, -0.5,  0.5, 0, 0,     #vertix 3

            # Face 3 Triangulo 1
            -0.5,  0.5,  0.5, 1, 0,     #vertix 1
            -0.5,  0.5, -0.5, 1, 1,     #vertix 2
            -0.5, -0.5, -0.5, 0, 1,     #vertix 3

            # Face 3 Triangulo 2
            -0.5, -0.5, -0.5, 0, 1,     #vertix 1
            -0.5, -0.5,  0.5, 0, 0,     #vertix 2
            -0.5,  0.5,  0.5, 1, 0,     #vertix 3

            # Face 4 Triangulo 1
             0.5,  0.5,  0.5, 1, 0,     #vertix 1
             0.5,  0.5, -0.5, 1, 1,     #vertix 2
             0.5, -0.5, -0.5, 0, 1,     #vertix 3

            # Face 4 Triangulo 2
             0.5, -0.5, -0.5, 0, 1,     #vertix 1
             0.5, -0.5,  0.5, 0, 0,     #vertix 2
             0.5,  0.5,  0.5, 1, 0,     #vertix 3

            # Face 5 Triangulo 1
            -0.5, -0.5, -0.5, 0, 1,     #vertix 1
             0.5, -0.5, -0.5, 1, 1,     #vertix 2
             0.5, -0.5,  0.5, 1, 0,     #vertix 3

            # Face 5 Triangulo 2
             0.5, -0.5,  0.5, 1, 0,     #vertix 1
            -0.5, -0.5,  0.5, 0, 0,     #vertix 2
            -0.5, -0.5, -0.5, 0, 1,     #vertix 3

            # Face 6 Triangulo 1
            -0.5,  0.5, -0.5, 0, 1,     #vertix 1
             0.5,  0.5, -0.5, 1, 1,     #vertix 2
             0.5,  0.5,  0.5, 1, 0,     #vertix 3

            # Face 6 Triangulo 2
             0.5,  0.5,  0.5, 1, 0,     #vertix 1
            -0.5,  0.5,  0.5, 0, 0,     #vertix 2
            -0.5,  0.5, -0.5, 0, 1      #vertix 3
        )

        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertex_count = len(self.vertices) // 5

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao) #Irá definir os vertices

        # Guarda num buffer inbutido no openGL os vertices em bytes e defina a forma de acessá-los (GL_STATIC_DRAW)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        #Posição dos vertices
        glEnableVertexAttribArray(0)
        #24 bytes para cada vertice (cada ponto são 4 bytes logo 6*4)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        # ctypes.c_void_p(12)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))



    #Limpar a memoria utilizada do triangulo
    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))


class Material:
    #Coordenada da textura S(esquerda(0) e direita(1)) e T(cima(0) e baixo(1))
    def __init__(self, filepath):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) #Quando estiver a diminuir a textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) #Quando estiver a aumentar a textura

        image = pg.image.load(filepath).convert_alpha()
        image_width, image_height = image.get_rect().size
        #Converter a imagem do pygame para OpenGL
        image_data = pg.image.tostring(image, "RGBA")
        glTexImage2D(GL_TEXTURE_2D, 0,GL_RGBA, image_width, image_height, 0,GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)

    def use(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def destroy(self):
        glDeleteTextures(1, (self.texture,))


class App:

    def __init__(self):

        pg.init()
        pg.display.set_mode((840, 620), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(.1, .2, .2, 1)
        glEnable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.shader = self.createShader("shaders/vertex.txt", "shaders/fragment.txt")
        glUseProgram(self.shader)
        glUniform1i(glGetUniformLocation(self.shader, "imageTexture"), 0)

        self.cube = Cube(
            position=[0, 0, -3],
            eulers=[0, 0, 0]
        )

        self.cube_mesh = CubeMesh()

        self.extreme_texture = Material("gfx/extreme.png")

        projection_transform = pyrr.matrix44.create_perspective_projection(
            fovy=45,
            aspect=840/620,
            near=.1,
            far=10,
            dtype=np.float32
        )

        glUniformMatrix4fv(
            glGetUniformLocation(self.shader, "projection"),
            1, GL_FALSE, projection_transform
        )

        self.modelMatrixLocation = glGetUniformLocation(self.shader, "model")

        self.mainLoop()

    def createShader(self, vertexFilepath, fragmentFilepath):

        with open(vertexFilepath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilepath, 'r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER),
        )
        return shader

    def mainLoop(self):

        running = True

        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            #Update cube x=0 y=2 z=1
            self.cube.eulers[2] += 0.2
            if self.cube.eulers[2] > 360:
                self.cube.eulers[2] -= 360

            #Refresh screen
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glUseProgram(self.shader)
            self.extreme_texture.use()

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)

            #Rotate around origin
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform,
                m2=pyrr.matrix44.create_from_eulers(
                    eulers=np.radians(self.cube.eulers),
                    dtype=np.float32
                )
            )

            #Define a posicao
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform,
                m2=pyrr.matrix44.create_from_translation(
                    vec=self.cube.position,
                    dtype=np.float32
                )
            )

            glUniformMatrix4fv(self.modelMatrixLocation, 1, GL_FALSE, model_transform)
            glBindVertexArray(self.cube_mesh.vao)
            glDrawArrays(GL_TRIANGLES, 0, self.cube_mesh.vertex_count)

            pg.display.flip()
            self.clock.tick(60)
        self.quit()

    def quit(self):
        self.cube_mesh.destroy()
        self.extreme_texture.destroy()
        glDeleteProgram(self.shader)
        pg.quit()


if __name__ == "__main__":
    myApp = App()
