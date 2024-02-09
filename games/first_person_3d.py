from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)

        # Scale and position the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Add the task to the task manager.
        self.taskMgr.add(self.move, "moveTask")

        # Define the key inputs.
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("arrow_down", self.setKey, ["backward", True])
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])
        self.accept("arrow_down-up", self.setKey, ["backward", False])

        # Initialize key map.
        self.keyMap = {"left": False, "right": False, "forward": False, "backward": False}

    # Records the state of the arrow keys.
    def setKey(self, key, value):
        self.keyMap[key] = value

    # Defines the task to move the camera.
    def move(self, task):
        speed = 25.0
        dt = globalClock.getDt()

        if self.keyMap["left"]:
            self.camera.setX(self.camera, -speed*dt)
        if self.keyMap["right"]:
            self.camera.setX(self.camera, speed*dt)
        if self.keyMap["forward"]:
            self.camera.setY(self.camera, -speed*dt)
        if self.keyMap["backward"]:
            self.camera.setY(self.camera, speed*dt)

        return Task.cont

app = MyApp()
app.run()