import numpy as np
import math
import pathlib
import sys

import pygame

from geometry.areia import AreiaGeometry
from geometry.bal import BalGeometry
from geometry.berlin_massa import BerlinMassaGeometry
from geometry.berlin_recheio import BerlinRecheioGeometry
from geometry.calcao import CalcaoGeometry
from geometry.madeira_bancos import MadeiraGeometry
from geometry.niandertal import NiandertalGeometry
from geometry.panamafita import PanamaFitaGeometry
from geometry.parteAmarela import parteAmarela
from geometry.parteAzul import parteAzul
from geometry.parteBranca import parteBranca
from geometry.panama import PanamaGeometry
from geometry.parteVerde import parteVerde
from geometry.parteVermelha import parteVermelha
from geometry.sphere import SphereGeometry
from geometry.rectangle import RectangleGeometry
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from extras.movement_rig import MovementRig
from geometry.vigas_banco import VigasGeometry
from material.texture import TextureMaterial


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

        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="images/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)

        bola_berlim_massa = BerlinMassaGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/berlin_massa.jpg"))
        self.bola_Berlim = Mesh(bola_berlim_massa, material1)
        bola_berlim_recheio = BerlinRecheioGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/berlin_recheio.png"))
        self.bola_Berlim.add(Mesh(bola_berlim_recheio,material1))
        self.bola_Berlim.translate(0.7,0.27,0)
        self.scene.add(self.bola_Berlim)

        areia_plano = AreiaGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="Objetos/Cena1/Plano/textures/daniel-straub-n5HOJGtYt4Q-unsplash.jpg"))
        self.areia = Mesh(areia_plano, material1)
        self.areia.scale(0.5)
        self.areia.translate(0,-4,0)
        self.scene.add(self.areia)

        madeira_bancos = MadeiraGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/bench.jpg"))
        self.bancos = Mesh(madeira_bancos, material1)
        vigas_bancos = VigasGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/vigas.jpeg"))
        self.bancos.add(Mesh(vigas_bancos, material1))
        self.bancos.translate(0.7, 0.27, 0)
        self.scene.add(self.bancos)

        bola = parteVermelha()
        material1 = TextureMaterial(texture=Texture(file_name="images/vermelho.jpg"))
        mesh1 = Mesh(bola, material1)
        mesh1.set_position([0,0.8,0])
        self.bola_mesh = mesh1


        bola = parteAzul()
        material1 = TextureMaterial(texture=Texture(file_name="images/azul.jpg"))
        mesh1 = Mesh(bola, material1)
        self.bola_mesh.add(mesh1)


        bola = parteVerde()
        material1 = TextureMaterial(texture=Texture(file_name="images/verde.jpg"))
        mesh1 = Mesh(bola, material1)
        self.bola_mesh.add(mesh1)


        bola = parteBranca()
        material1 = TextureMaterial(texture=Texture(file_name="images/white.png"))
        mesh1 = Mesh(bola, material1)
        self.bola_mesh.add(mesh1)

        bola = parteAmarela()
        material1 = TextureMaterial(texture=Texture(file_name="images/amarelo.jpg"))
        mesh1 = Mesh(bola, material1)
        self.bola_mesh.add(mesh1)
        self.bola_mesh.scale(0.5)
        self.scene.add(self.bola_mesh)

        calcao_geometria = CalcaoGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/textura_calcao.png"))
        self.calcao = Mesh(calcao_geometria,material1)
        self.calcao.scale(0.4)
        self.calcao.translate(-0.1,0.05,-1)
        self.scene.add(self.calcao)

        flipflop = PanamaGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/panamatexture.jpeg"))
        mesh2 = Mesh(flipflop, material1)
        mesh2.set_position([0,2,0])
        self.chapeu_mesh2 = mesh2
        fita = PanamaFitaGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/panamafitatexture.jpg"))
        self.chapeu_mesh2.add(Mesh(fita, material1))
        self.chapeu_mesh2.scale(0.6)
        self.chapeu_mesh2.translate(0.1,-0.7,0)
        self.chapeu_mesh2.rotate_z(-0.1)
        self.scene.add(self.chapeu_mesh2)

        #TODO Colocar o conteudo da geometry de baliza, niandertal(talvez), e octane
 
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="Objetos/Cena1/Plano/textures/daniel-straub-n5HOJGtYt4Q-unsplash.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
        self.scene.add(grass)
        self.camera_move = 0.1
        self.scene.add(self.rig)
        self.object = self.bola_mesh

        baliza = BalGeometry()
        material1 = TextureMaterial(texture=Texture(file_name="images/campo.png"), property_dict={"doubleSide": True})
        self.balizaScene = Mesh(baliza, material1)
        self.balizaScene.rotate_y(90)
        self.scene.add(self.balizaScene)
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
        if "m" in self.input.key_pressed_list:
            self.camera.rotate_y(-0.01)
        if "," in self.input.key_pressed_list:
            self.camera.rotate_y(0.01)
        if "1" in self.input.key_pressed_list:
            self.object = self.bola_mesh
        if "2" in self.input.key_pressed_list:
            self.object = self.chapeu_mesh2
        if "3" in self.input.key_pressed_list:
            self.object = self.bola_Berlim
        if "4" in self.input.key_pressed_list:
            self.object = self.calcao
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
