from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from panda3d.core import WindowProperties



loadPrcFileData(" ", """ 
window-title Game
win-size 1280 720
fullscreen false    
""")



class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        #windows properties
        props = WindowProperties()
        props.setFixedSize(False)
        self.win.requestProperties(props)

        





game = MyApp()
game.run()


