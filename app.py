from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
for z in range(20):
    for x in range(20):
        Entity(
           parent=scene,
            position=(x,0,z),
            origin_y =0.5,
            color = color.rgb(255,255,255),
            texture= 'texture/grass.jpg',
            model = 'cube',
            collider = 'box',
            ignore = True,
            text = 'white cube'
        )
class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            origin_y =0.5,
            color = color.rbg(0,0,1),
            texture= 'texture/grass.jpg',
            model = 'cube'
        )
        self.texture_index = 0
        self.texture = ['grass.jpg']
    def input(self, key):
        return None
TextureBox()
if __name__ == '__main__':
    app.run()