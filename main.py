import numpy as np
import math
import pathlib
import sys
import time
import pygame

from pygame import mixer


from extras.directional_light import DirectionalLightHelper
from geometry.arvores import *
from geometry.campo import *
from geometry.berlin import *
from geometry.bancos import *
from geometry.humano import *
from geometry.bola import *
from geometry.octane import *
from geometry.pedras import PedrasGeometry, FalesiaGeometry
from geometry.sphere import SphereGeometry
from geometry.rectangle import RectangleGeometry
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from extras.movement_rig import MovementRig
from light.ambient import AmbientLight
from light.directional import DirectionalLight
from light.point import PointLight
from light.shadow import Shadow
from material.flat import FlatMaterial
from material.lambert import LambertMaterial
from material.phong import PhongMaterial
from material.texture import TextureMaterial

#Mudar para a quantidade de luzes que formos utilizar
number_of_lights=2

def create_mesh(geometry, filename):
    material = TextureMaterial(texture=Texture(file_name=filename))
    return Mesh(geometry, material)

def create_phong_mesh(geometry, filename):
    material = PhongMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1, 1, 1]}, number_of_light_sources=number_of_lights,
            bump_texture=Texture(file_name="UV/Sand_004_Normal.png"))
    return Mesh(geometry, material)

def create_lambert_mesh(geometry, filename):
    material = LambertMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1, 1, 1]}, number_of_light_sources=number_of_lights, use_shadow=True)
    return Mesh(geometry, material)

def create_flat_mesh(geometry, filename):
    material = FlatMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1, 1, 1]}, number_of_light_sources=number_of_lights)
    return Mesh(geometry, material)

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add box movement: WASDRF(move), QE(turn), TG(look up and down).
    """

    def __init__(self, screen_size=(1920, 1080)):
        super().__init__(screen_size)
        self.animation = None
        self.rig_size = None
        self.currentObject = 0
        self.octane_index = None
        self.octane_rodas_tras_index = None
        self.octane_rodas_frente_index = None
        self.humano_index = None
        self.bola_Berlim_index = None
        self.bola_index = None
        self.index_not_move = list()
        self.xRecorded = None
        self.yRecorded = None
        self.zRecorded = None
        self.move = 0
        self.rot = 1

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0.5, 1, 3])


        mixer.init()
        MusicaRocket = mixer.Sound("Music/Slushii - All I Need [Rocket League Intro Song] (2).mp3")
        MusicaRocket.set_volume(0.2)
        Motor = mixer.Sound("Music/motor.mp3")
        MusicaRocket.play()
        Motor.set_volume(0.05)
        self.rig = []

        sky = create_mesh(SphereGeometry(radius=50), "Objetos/Texturas/Ambiente/sky.jpg")
        self.scene.add(sky)

        self.bola_Berlim = create_phong_mesh(BerlinExplosaoMassaGeometry(), "Objetos/Texturas/Humano/Berlin_massa.jpg")
        self.bola_Berlim.add(create_phong_mesh(BerlinExplosaoRecheioGeometry(), "Objetos/Texturas/Humano/Berlin_recheio.png"))
        self.scene.add(self.bola_Berlim)
        self.rig.append(MovementRig())
        self.bola_Berlim_index = len(self.rig)-1
        self.rig[self.bola_Berlim_index].add(self.bola_Berlim)

        self.bancos = create_phong_mesh(MadeiraGeometry(), "Objetos/Texturas/Bancos/bench.jpg")
        self.bancos.add(create_phong_mesh(TubosGeometry(), "Objetos/Texturas/Bancos/vigas.jpeg"))
        self.scene.add(self.bancos)

        self.bola = create_phong_mesh(BolaParteVermelha(), "Objetos/Texturas/Bola/vermelho.jpg")
        self.bola.add(create_phong_mesh(BolaParteAzul(), "Objetos/Texturas/Bola/azul.jpg"))
        self.bola.add(create_phong_mesh(BolaParteBranca(), "Objetos/Texturas/Bola/branco.png"))
        self.bola.add(create_phong_mesh(BolaParteVerde(), "Objetos/Texturas/Bola/verde.jpg"))
        self.bola.add(create_phong_mesh(BolaParteAmarela(), "Objetos/Texturas/Bola/amarelo.jpg"))
        self.scene.add(self.bola)
        self.rig.append(MovementRig())
        self.bola_index = len(self.rig) - 1
        self.rig[self.bola_index].add(self.bola)

        self.humano = create_phong_mesh(CalcaoGeometry(), "Objetos/Texturas/Humano/Calcoes_textura.png")
        self.humano.add(create_phong_mesh(HumanoCorpoGeometry(), "Objetos/Texturas/Humano/Pele.PNG"))
        self.humano.add(create_phong_mesh(HumanoDentesGeometry(), "Objetos/Texturas/Humano/Dentes.png"))
        self.humano.add(create_phong_mesh(HumanoLinguaGeometry(), "Objetos/Texturas/Humano/Lingua.png"))
        self.humano.add(create_phong_mesh(HumanoCabeloGeometry(), "Objetos/Texturas/Humano/PretoCabelo.png"))
        #self.humano.add(create_phong_mesh(HumanoOculosGeometry(), "Objetos/Texturas/Humano/PretoOculos.png"))
        self.humano.add(create_phong_mesh(BerlinComerMassaGeometry(), "Objetos/Texturas/Humano/Berlin_massa.jpg"))
        self.humano.add(create_phong_mesh(BerlinComerRecheioGeometry(), "Objetos/Texturas/Humano/Berlin_recheio.png"))
        self.humano.set_position((-20, 0, 0))
        self.scene.add(self.humano)
        self.rig.append(MovementRig())
        self.humano_index = len(self.rig) - 1
        self.rig[self.humano_index].add(self.humano)

        self.octane = create_phong_mesh(PanamaGeometry(), "Objetos/Texturas/Octane/Panama.jpeg")
        self.octane.add(create_phong_mesh(PanamaFitaGeometry(), "Objetos/Texturas/Octane/PanamaFita.jpg"))
        self.octane.add(create_phong_mesh(OctaneMotorGeometry(), "Objetos/Texturas/Octane/Motor.png"))
        self.octane.add(create_phong_mesh(OctaneCarcacaGeometry(), "Objetos/Texturas/Octane/ParteVermelha.png"))
        self.octane.add(create_phong_mesh(OctaneJanelaGeometry(), "Objetos/Texturas/Octane/Preto.png"))
        self.octane.add(create_phong_mesh(OctaneLinhasGeometry(), "Objetos/Texturas/Octane/Preto.png"))

        self.rodasFrente = create_phong_mesh(RodasFrenteGeometry(), "Objetos/Texturas/Octane/Preto.png")
        self.rig.append(MovementRig())
        self.octane_rodas_frente_index = len(self.rig) - 1
        self.index_not_move.append(self.octane_rodas_frente_index)
        self.rig[self.octane_rodas_frente_index].add(self.rodasFrente)

        self.rodasAtras = create_phong_mesh(RodasTrasGeometry(), "Objetos/Texturas/Octane/Preto.png")
        self.rig.append(MovementRig())
        self.octane_rodas_tras_index = len(self.rig) - 1
        self.index_not_move.append(self.octane_rodas_tras_index)
        self.rig[self.octane_rodas_tras_index].add(self.rodasAtras)

        self.octane.add(self.rodasFrente)
        self.octane.add(self.rodasAtras)
        self.scene.add(self.octane)
        self.rig.append(MovementRig())
        self.octane_index = len(self.rig) - 1
        self.rig[self.octane_index].add(self.octane)

        self.pedras = create_phong_mesh(PedrasGeometry(), "Objetos/Texturas/Ambiente/rock.png")
        self.scene.add(self.pedras)

        self.arvores = create_phong_mesh(MadeiraArvoresGeometry1(), "Objetos/Texturas/Ambiente/palmtree_wood.jpg")
        self.arvores.add(create_phong_mesh(MadeiraArvoresGeometry2(), "Objetos/Texturas/Ambiente/palmtree_wood.jpg"))
        self.arvores.add(create_phong_mesh(MadeiraArvoresGeometry3(), "Objetos/Texturas/Ambiente/palmtree_wood.jpg"))
        self.arvores.add(create_phong_mesh(MadeiraArvoresGeometry4(), "Objetos/Texturas/Ambiente/palmtree_wood.jpg"))

        self.arvores.add(create_phong_mesh(FolhasGeometry1(), "Objetos/Texturas/Ambiente/palmtree_leaf.png"))
        self.arvores.add(create_phong_mesh(FolhasGeometry2(), "Objetos/Texturas/Ambiente/palmtree_leaf.png"))
        self.arvores.add(create_phong_mesh(FolhasGeometry3(), "Objetos/Texturas/Ambiente/palmtree_leaf.png"))
        self.arvores.add(create_phong_mesh(FolhasGeometry4(), "Objetos/Texturas/Ambiente/palmtree_leaf.png"))

        self.scene.add(self.arvores)



        self.cliff = create_lambert_mesh(FalesiaGeometry(), "Objetos/Texturas/Ambiente/cliff.jpg")
        self.scene.add(self.cliff)




        sea_material = LambertMaterial(
            texture=Texture(file_name="Objetos/Texturas/Ambiente/mar.jpg"),
            number_of_light_sources=number_of_lights,
            use_shadow=True,
            bump_texture=Texture(file_name="UV/Sand_004_Normal.png")
        )
        self.sea = Mesh(RectangleGeometry(width=100, height=100), sea_material)
        self.sea.set_position([65, 4, 0])
        self.sea.rotate_z(0.1)
        self.sea.rotate_x(-math.pi / 2)
        self.scene.add(self.sea)

        sand_material = LambertMaterial(
            texture=Texture(file_name="Objetos/Texturas/Ambiente/sand.jpg"),
            number_of_light_sources=number_of_lights,
            use_shadow =True,
            bump_texture=Texture(file_name="UV/Sand_004_Normal.png")
        )
        self.sand = Mesh(RectangleGeometry(width=100, height=100), sand_material)
        self.sand.rotate_x(-math.pi/2)
        self.scene.add(self.sand)


        self.campo = create_mesh(BalizaAzulGeometry(), "Objetos/Texturas/Baliza/ParteAzul.png")
        self.campo.add(create_mesh(BalizaVermelhoGeometry(), "Objetos/Texturas/Baliza/ParteVermelha.png"))
        self.campo.add(create_mesh(BalizaBrancoGeometry(), "Objetos/Texturas/Baliza/ParteBranca.png"))
        self.campo.add(create_mesh(CampoPartePretaGeometry(), "Objetos/Texturas/Estadio/PartePreta.png"))
        self.campo.add(create_mesh(CampoParteAzulGeometry(), "Objetos/Texturas/Estadio/ParteAzul.png"))
        self.campo.add(create_mesh(CampoTransparenteGeometry(), "Objetos/Texturas/Estadio/ParteTransparente.png"))
        self.scene.add(self.campo)

        self.ambient_light = AmbientLight(color=[0.3, 0.3, 0.3])
        self.scene.add(self.ambient_light)
        self.directional_light = DirectionalLight(color=(0.8, 0.8, 0.8), direction=[0, -0.5, 0])
        self.scene.add(self.directional_light)
        self.renderer.enable_shadows(self.directional_light)
        # The directional light can take any position because it covers all the space.
        # The directional light helper is a child of the directional light.
        # So changing the global matrix of the parent leads to changing
        # the global matrix of its child.
        self.directional_light.set_position([0, 2, 0])


        self.camera_move = 0.1
        self.rig_size = len(self.rig)
        for i in range(self.rig_size):
            self.scene.add(self.rig[i])
        self.currentObject = 0
        self.cameraMovements = []
        for i in range(180):
            self.cameraMovements.append([0, 0, -0.011, [-0.002, True], [0, True], [0, True]])
        for i in range(80):
            self.cameraMovements.append([0, 0, 0, [0, True], [-math.pi/100, False], [0, True]])
        for i in range(20):
            self.cameraMovements.append([-0.03, 0, 0, [0, True], [-math.pi / 100, False], [0, True]])
        self.j = 0

        print("Troca de objeto no 1, 2, 3 e 4.")
        print("Camera h, j, k, l, u, n, t, g.")
        print("Ojeto w, a, s, d, q, e, r, f, z, x.")
        print("berlin: " + str(self.bola_Berlim_index), "humano: " + str(self.humano_index))
        print("bola: " + str(self.bola_index), "octane: " + str(self.octane_index))

        self.play = False
        # move ou rot, object, dist ou angle, time
        # music, time to start, time to end
        self.animation = [[self.move, self.octane_index, [0.5, 0, 0], 0.5],
                          [self.move, self.bola_index, [0, 0, 0], 0.5],
                          [self.move, self.octane_index, [1.1, 0, 0], 1.1],
                          [self.move, self.bola_index, [1.1, 0.8, 0], 0.4],
                          [self.move, self.bola_index, [1.07, 0.5, 0], 0.4],
                          [self.move, self.bola_index, [1.07, 0.3, 0], 0.8],
                          [self.move, self.bola_index, [1.07, -0.05, 0], 0.8],
                          [self.move, self.bola_index, [1.07, -0.1, 0], 1.2],
                          [self.move, self.bola_index, [1.07, -0.15, 0], 1.5],
                          [self.move, self.bola_index, [1.07, -0.3, 0], 2],
                          [self.move, self.bola_index, [-0.4, -0.2, 0], 0.5],
                          [self.move, self.octane_index, [0, 0, 0], 5],
                          [self.move, self.octane_index, [0.7, 0, 0], 0.4],
                          [self.move, self.octane_index, [2.0, 0, 0], 0.6],
                          [self.move, self.octane_index, [0.9, 0.3, 0], 0.5],
                          [self.move, self.bola_index, [-0.5, -0.2, 0], 1.5],
                          [self.move, self.octane_index, [0.9, 0.2, 0], 1.5],
                          [self.move, self.bola_index, [-0.3, -0.1, 0], 4],
                          [self.move, self.octane_index, [0.7, 0.1, 0], 4],
                          [self.move, self.bola_index, [1.5, -0.2, 0], 0.8],
                          [self.move, self.octane_index, [0.4, 0.3, 0], 0.8],
                          [self.move, self.bola_index, [0, -1.1, 0], 0],
                          [self.move, self.octane_index, [-3.2, 1.6, 0], 0.5],
                          [self.move, self.bola_Berlim_index, [0, 0, 0], 14.4],
                          [self.move, self.bola_Berlim_index, [17, 0, 0], 0],
                          [self.move, self.bola_Berlim_index, [-0.6, 0, 0], 0.5],
                          [self.move, self.octane_index, [-1.9, 0.7, 0], 0.8],
                          [self.move, self.bola_Berlim_index, [-1.7, 1.1, 0], 0.8],
                          ]

    def update(self):
        if "," in self.input.key_down_list:
            self.rig[self.octane_index].translate(-self.rig[self.octane_index].global_position[0],
                                                  -self.rig[self.octane_index].global_position[1],
                                                  -self.rig[self.octane_index].global_position[2])
            self.rig[self.bola_index].translate(-self.rig[self.bola_index].global_position[0],
                                                -self.rig[self.bola_index].global_position[1],
                                                -self.rig[self.bola_index].global_position[2])
            self.rig[self.bola_Berlim_index].translate(-self.rig[self.bola_Berlim_index].global_position[0],
                                                       -self.rig[self.bola_Berlim_index].global_position[1],
                                                       -self.rig[self.bola_Berlim_index].global_position[2])
            for i in range(len(self.animation)):
                if self.animation[i][0] == self.move:
                    self.rig[self.animation[i][1]].move(self.animation[i][2], self.animation[i][3])
                if self.animation[i][0] == self.rot:
                    self.rig[self.animation[i][1]].rotate(self.animation[i][2], self.animation[i][3])
        if "p" in self.input.key_pressed_list:
            self.play = True
        if self.play:
            if self.j < len(self.cameraMovements):
                movimento = self.cameraMovements[self.j]
                self.camera.translate(movimento[0], movimento[1], movimento[2])
                self.camera.rotate_x(movimento[3][0], movimento[3][1])
                self.camera.rotate_y(movimento[4][0], movimento[4][1])
                self.camera.rotate_z(movimento[5][0], movimento[5][1])
                self.j += 1
        for i in range(self.rig_size):
            self.rig[i].update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
        if "a" in self.input.key_pressed_list:
            self.camera.translate(-self.camera_move,0,0)
        if "left shift" in self.input.key_pressed_list:
            self.camera.translate(0,-self.camera_move,0)
        if "space" in self.input.key_pressed_list:
            self.camera.translate(0,self.camera_move,0)
        if "d" in self.input.key_pressed_list:
            self.camera.translate(self.camera_move,0,0)
        if "w" in self.input.key_pressed_list:
            self.camera.translate(0,0,-self.camera_move)
        if "s" in self.input.key_pressed_list:
            self.camera.translate(0,0,self.camera_move)
        if "t" in self.input.key_pressed_list:
            self.camera.rotate_x(-0.01)
        if "g" in self.input.key_pressed_list:
            self.camera.rotate_x(0.01)
        if "e" in self.input.key_pressed_list:
            self.camera.rotate_y(-0.01)
        if "q" in self.input.key_pressed_list:
            self.camera.rotate_y(0.01)
        if "r" in self.input.key_down_list:
            self.currentObject = (self.currentObject+1) % self.rig_size
            while self.currentObject in self.index_not_move:
                self.currentObject = (self.currentObject+1) % self.rig_size
            print(self.currentObject)
            self.xRecorded = self.rig[self.currentObject].global_position[0]
            self.yRecorded = self.rig[self.currentObject].global_position[1]
            self.zRecorded = self.rig[self.currentObject].global_position[2]
        if "left" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(-0.1,0,0)
        if "up" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(0,0,-0.1)
        if "right" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(0.1,0,0)
        if "down" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(0,0,0.1)
        if "o" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(0,0.1,0)
        if "l" in self.input.key_pressed_list:
            self.rig[self.currentObject].translate(0,-0.1,0)
        if "k" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_x(0.01, local=False)
        if "j" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_x(-0.01, local=False)
        if "y" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_z(0.01, local=False)
        if "h" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_z(-0.01, local=False)
        if "u" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_y(0.01, local=False)
        if "i" in self.input.key_pressed_list:
            self.rig[self.currentObject].rotate_y(-0.01, local=False)
        if "escape" in self.input.key_pressed_list:
            self.input._quit = True
        if "1" in self.input.key_down_list:
            self.xRecorded = self.rig[self.currentObject].global_position[0]
            self.yRecorded = self.rig[self.currentObject].global_position[1]
            self.zRecorded = self.rig[self.currentObject].global_position[2]
        if "2" in self.input.key_down_list:
            x_move = str('x: ') + str(round((self.rig[self.currentObject].global_position[0] - self.xRecorded)*100)/100)
            y_move = str('y: ') + str(round((self.rig[self.currentObject].global_position[1] - self.yRecorded)*100)/100)
            z_move = str('z: ') + str(round((self.rig[self.currentObject].global_position[2] - self.zRecorded)*100)/100)
            print(x_move, y_move, z_move)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
