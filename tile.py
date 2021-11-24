class Tile:
    def __init__(self, val, vis=False):
        self.value = val
        self.visible = vis
        self.flag_state = False

    def flip(self):
        self.visible = True

    def flag(self):
        self.flag_state = not self.flag_state

    def setValue(self, val):
        self.value = val

    def __repr__(self):
        if self.visible:
            return self.value
        elif self.flag_state:
            return 'F'
        else:
            return 'X'  

class Bomb(Tile):
    def __init__(self, vis=False):
        self.exploded = False
        super().__init__('M', vis)

