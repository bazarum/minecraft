from .object import Object


class Wall(Object):
    height = 5
    length = 10
    width = 2
    backwards = False

    def build(self):
        self.server.setBlocks(
            self.position.x, self.position.y, self.position.z,
            self.position.x+self.length-1,
            self.position.y+self.height-1,
            self.position.z+self.width-1,
            self.block)