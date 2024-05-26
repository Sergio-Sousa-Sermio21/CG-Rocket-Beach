import numpy as np
import math
import pathlib
import sys

import pygame

from extras.directional_light import DirectionalLightHelper
from geometry.campo import *
from geometry.berlin import *
from geometry.bancos import *
from geometry.humano import *
from geometry.bola import *
from geometry.octane import *
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
    material = PhongMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1,1, 1]}, number_of_light_sources=number_of_lights)
    return Mesh(geometry, material)

def create_lambert_mesh(geometry, filename):
    material = LambertMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1, 1, 1]}, number_of_light_sources=number_of_lights)
    return Mesh(geometry, material)

def create_flat_mesh(geometry, filename):
    material = FlatMaterial(texture=Texture(file_name=filename), property_dict={"baseColor": [1, 1, 1]}, number_of_light_sources=number_of_lights)
    return Mesh(geometry, material)

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add box movement: WASDRF(move), QE(turn), TG(look).
    """

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0.5, 1, 3])

        self.rig = MovementRig()
        self.rig.set_position([0, 0.5, -0.5])

        sky = create_mesh(SphereGeometry(radius=50), "Objetos/Texturas/Ambiente/sky.jpg")
        self.scene.add(sky)

        self.bola_Berlim = create_phong_mesh(BerlinComerMassaGeometry(), "Objetos/Texturas/Humano/Berlin_massa.jpg")
        self.bola_Berlim.add(create_phong_mesh(BerlinComerRecheioGeometry(), "Objetos/Texturas/Humano/Berlin_recheio.png"))
        self.scene.add(self.bola_Berlim)

        self.bancos = create_phong_mesh(MadeiraGeometry(), "Objetos/Texturas/Bancos/bench.jpg")
        self.bancos.add(create_phong_mesh(TubosGeometry(), "Objetos/Texturas/Bancos/vigas.jpeg"))
        self.scene.add(self.bancos)

        self.bola = create_phong_mesh(BolaParteVermelha(), "Objetos/Texturas/Bola/vermelho.jpg")
        self.bola.add(create_phong_mesh(BolaParteAzul(), "Objetos/Texturas/Bola/azul.jpg"))
        self.bola.add(create_phong_mesh(BolaParteBranca(), "Objetos/Texturas/Bola/branco.png"))
        self.bola.add(create_phong_mesh(BolaParteVerde(), "Objetos/Texturas/Bola/verde.jpg"))
        self.bola.add(create_phong_mesh(BolaParteAmarela(), "Objetos/Texturas/Bola/amarelo.jpg"))
        self.scene.add(self.bola)

        self.humano = create_phong_mesh(CalcaoGeometry(), "Objetos/Texturas/Humano/Calcoes_textura.png")
        self.humano.add(create_phong_mesh(HumanoCorpoGeometry(), "Objetos/Texturas/Humano/Pele.PNG"))
        self.humano.add(create_phong_mesh(HumanoDentesGeometry(), "Objetos/Texturas/Humano/Dentes.png"))
        self.humano.add(create_phong_mesh(HumanoLinguaGeometry(), "Objetos/Texturas/Humano/Lingua.png"))
        self.humano.add(create_phong_mesh(HumanoCabeloGeometry(), "Objetos/Texturas/Humano/PretoCabelo.png"))
        self.humano.add(create_phong_mesh(HumanoOculosGeometry(), "Objetos/Texturas/Humano/PretoOculos.png"))
        self.scene.add(self.humano)

        self.octane = create_phong_mesh(PanamaGeometry(), "Objetos/Texturas/Octane/Panama.jpeg")
        self.octane.add(create_phong_mesh(PanamaFitaGeometry(), "Objetos/Texturas/Octane/PanamaFita.jpg"))
        self.octane.add(create_phong_mesh(OctaneMotorGeometry(), "Objetos/Texturas/Octane/Motor.png"))
        self.octane.add(create_phong_mesh(OctaneCarcacaGeometry(), "Objetos/Texturas/Octane/ParteVermelha.png"))
        self.octane.add(create_phong_mesh(OctaneJanelaGeometry(), "Objetos/Texturas/Octane/Preto.png"))
        self.octane.add(create_phong_mesh(OctaneLinhasGeometry(), "Objetos/Texturas/Octane/Preto.png"))

        self.rodasFrente = create_phong_mesh(RodasFrenteGeometry(), "Objetos/Texturas/Octane/Preto.png")
        self.rodasAtras = create_phong_mesh(RodasTrasGeometry(), "Objetos/Texturas/Octane/Preto.png")
        self.octane.add(self.rodasFrente)
        self.octane.add(self.rodasAtras)
        self.scene.add(self.octane)

        ambient_light = AmbientLight(color=[0.1, 0.1, 0.1])
        self.scene.add(ambient_light)
        self.directional_light = DirectionalLight(color=(0.8, 0.8, 0.8),direction=[0,-0.5, 0])
        self.scene.add(self.directional_light)

        sand_material = LambertMaterial(
            texture=Texture(file_name="Objetos/Texturas/Ambiente/sand.jpg"),
            number_of_light_sources=number_of_lights
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

        self.camera_move = 0.1
        self.scene.add(self.rig)
        self.object = self.bola

        directional_light_helper = DirectionalLightHelper(self.directional_light)
        # The directional light can take any position because it covers all the space.
        # The directional light helper is a child of the directional light.
        # So changing the global matrix of the parent leads to changing
        # the global matrix of its child.
        self.directional_light.set_position([0, 2, 0])
        self.directional_light.add(directional_light_helper)
        print("Troca de objeto no 1, 2, 3 e 4.")
        print("Camera h, j, k, l, u, n, t, g.")
        print("Ojeto w, a, s, d, q, e, r, f, z, x.")

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)

        if "h" in self.input.key_pressed_list:
            self.camera.translate(-self.camera_move,0,0)
        if "j" in self.input.key_pressed_list:
            self.camera.translate(0,-self.camera_move,0)
        if "k" in self.input.key_pressed_list:
            self.camera.translate(0,self.camera_move,0)
        if "l" in self.input.key_pressed_list:
            self.camera.translate(self.camera_move,0,0)
        if "u" in self.input.key_pressed_list:
            self.camera.translate(0,0,-self.camera_move)
        if "n" in self.input.key_pressed_list:
            self.camera.translate(0,0,self.camera_move)
        if "t" in self.input.key_pressed_list:
            self.camera.rotate_x(-0.01)
        if "g" in self.input.key_pressed_list:
            self.camera.rotate_x(0.01)
        if "," in self.input.key_pressed_list:
            self.camera.rotate_y(-0.01)
        if "m" in self.input.key_pressed_list:
            self.camera.rotate_y(0.01)
        if "1" in self.input.key_pressed_list:
            self.object = self.bancos
        if "2" in self.input.key_pressed_list:
            self.object = self.humano
        if "3" in self.input.key_pressed_list:
            self.object = self.campo
        if "4" in self.input.key_pressed_list:
            self.object = self.octane
        if "a" in self.input.key_pressed_list:
            self.object.translate(-0.1,0,0)
        if "w" in self.input.key_pressed_list:
            self.object.translate(0,0,-0.1)
        if "d" in self.input.key_pressed_list:
            self.object.translate(0.1,0,0)
        if "s" in self.input.key_pressed_list:
            self.object.translate(0,0,0.1)
        if "r" in self.input.key_pressed_list:
            self.object.rotate_x(0.01)
        if "f" in self.input.key_pressed_list:
            self.object.rotate_x(-0.01)
        if "z" in self.input.key_pressed_list:
            self.object.rotate_z(0.01)
        if "x" in self.input.key_pressed_list:
            self.object.rotate_z(-0.01)
        if "q" in self.input.key_pressed_list:
            self.object.rotate_y(0.01)
        if "e" in self.input.key_pressed_list:
            self.object.rotate_y(-0.01)
        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
