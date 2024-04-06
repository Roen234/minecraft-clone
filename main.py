# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:41:07 2022

@author: roenr
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:41:07 4022

@author: roenr
"""
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', code='''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
from perlin_noise import PerlinNoise
import random
noise = PerlinNoise (octaves=3,seed=random.randint(1,1000000))
app = Ursina()
class Voxel(Button):
    def __init__(self,position=(0,0,0),texture='grass'):
        super().__init__(
            model='cube',
            parent=scene,
            color=color.white,
            origin_y=0.5,
            texture=texture,
            position=position,
            highlight_color=color.black,
            collider='cube')
    texture_num = 1

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                new = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
            if key == 'middle mouse down':
                self.texture_num += 1
                if self.texture_num > 7:
                    self.texture_num = 1
                if self.texture_num == 1:
                    self.texture = 'grass'
                elif self.texture_num == 2:
                    self.texture = 'dirt'
                elif self.texture_num == 3:
                    self.texture = 'brick'
                elif self.texture_num == 4:
                    self.texture = 'stone_brick'
                elif self.texture_num == 5:
                    self.texture = 'plank'
                elif self.texture_num == 6:
                    self.texture = 'gold'
                elif self.texture_num == 7:
                    self.texture = 'diamond_ore'
for z in range(50):
    for x in range(50):
        y = noise([x * .02,z * .02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x,y,z))
player = FirstPersonController(collider='box')
Sky()
app.run()

''')
if __name__ == '__main__':
    app.run(debug=True)