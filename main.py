from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData


loadPrcFileData(" ", """ 
window-title My Game
win-size 1280 720
fullscreen false    
""")



class MyApp(ShowBase):
    def __init__(self):
        super().__init__()







game = MyApp()
game.run()


