class Tile:
    ''' 
    A class that represents a tile within the minesweeper board
    ...
    
    Attributes
    ----------
    value: str
        Value of the tile
    
    visible: bool
        Whether or not the tile is revealed
    
    flag_state: bool
        Whether or not the tile is flagged

    Methods
    -------
    flip()
        Makes a tile object visible 
    
    flag()
        Toggles the flag_state of the tile object

    setValue(val)
        Sets the value of the tile
    '''
    def __init__(self, val, vis=False):
        '''Constructor

        Parameters
        ----------
        val: str
            Value of the tile
        vis: bool
            Whether or not the tile is revealed
        '''
        self.value = val        
        self.visible = vis       
        self.flag_state = False 

    def flip(self):
        ''' Reveals a tile'''
        self.visible = True

    def flag(self):
        '''Toggles the flag_state of the tile'''
        self.flag_state = not self.flag_state

    def setValue(self, val):
        '''Sets the value of the tile
        
        Parameters
        ----------
        val: str

        Returns
        -------
        None
        '''
        self.value = val

    def __repr__(self):
        if self.visible:
            return self.value
        elif self.flag_state:
            return 'F'
        else:
            return 'X'  

class Bomb(Tile):
    ''' 
    Class that represents a bomb tile in minesweeper. Subclass of tile.
    ...

    Attributes
    ----------
    Same as parent
    '''
    def __init__(self, vis=False):
        super().__init__('M', vis)

