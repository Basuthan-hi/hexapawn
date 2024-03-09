from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
block = 'object/block'
grass_texture = load_texture('assets/grass_block.png')
class Block(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent = scene,
			position = position,
			model = block,
			origin_y = 0.5,
			texture = grass_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5
        )
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                block = Block(position=self.position + mouse.normal)
            elif key == "right mouse down":
                destroy(self)

for z in range(20):
    for x in range(20):
        block = Block(position=(x,0,z))

player = FirstPersonController()
if __name__ == '__main__':
    app.run()