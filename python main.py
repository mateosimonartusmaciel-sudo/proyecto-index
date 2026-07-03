from ursina import *

app = Ursina()

# Texturas
block_texture = load_texture('white_cube')  
sky_texture = load_texture('sky_default')   
arm_texture = load_texture('arm_texture')   

# Clase de bloque
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=block_texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':   # Romper bloque
                destroy(self)
            if key == 'right mouse down':  # Colocar bloque
                Voxel(position=self.position + mouse.normal)

# Crear suelo
for z in range(20):
    for x in range(20):
        Voxel(position=(x,0,z))

# Jugador y entorno
player = FirstPersonController()
sky = Sky()
hand = Entity(model='cube', texture=arm_texture, scale=(0.2,0.4,0.2), position=(0.4,-0.6,0.6), rotation=(150,-10))

def update():
    hand.position = (0.4, -0.6, 0.6)
    hand.rotation = (150, -10)

app.run()