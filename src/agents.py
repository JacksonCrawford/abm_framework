from mesa import Agent
import mesa.space
from colour import Color

# cAMP agent, one is assigned per cell and it has the amoumt of cAMP
class cAMP(Agent):
    def __init__(self, pos, model, unique_id, amount, decRate):
        super().__init__(unique_id, model)
        self.pos = pos


# Slime Mold agent that interacts with the environment made up of cAMP agents
class SlimeAgent(Agent):
    def __init__(self, pos, model, unique_id, secRate, color):
        super().__init__(pos, model)
        self.pos = pos
        self.unique_id = unique_id
        self.color = color
        self.secRate = 2

        if color == "Red":
            self.shade = "#720000"
        elif color == "Green":
            self.shade = "#00741c"
        else:
            self.shade = "#4a7d8e"

        self.secRate = 1

        self.layer = 1

    # Get agent's Unique ID
    def getUniqueID(self):
        return self.unique_id

    # Get agent's X coord
    def getX(self):
        return self.pos[0]

    # Get agent's Y coord
    def getY(self):
        return self.pos[1]
        return self.layer

    # Get secretion rate
    def getSecRate(self):
        return self.secRate;

    # Increment layer by 1
    def addLayer(self):
        self.layer += 1

    # Set agent's Unique ID
    def setUniqueID(self, uParam):
        self.unique_id = uParam

    # Set agent's X coord
    def setX(self, xParam):
        self.x = xParam

    # Set agent's Y coord
    def setY(self, yParam):
        self.y = yParam

    # Set secretion rate
    def setSecRate(self, srParam):
        self.secRate = srParam

    # Get immediate neighbors without center or diagonals
    def getNeighbors(self):
        return self.model.grid.get_neighbors(self.pos, moore=False, include_center=False, radius=1)


    # Move to a specified position
    def move(self, newPos):
        self.model.grid.move_agent(self, newPos)

    # Set string colorname for agent
    def setColor(self, colorName):
        self.color = colorName

    # Set agent's shade in hex
    def setShade(self, hexCode):
        self.shade = hexCode

    # All step interaction is done with the environment, and is therefore calculated in the Model itself
    def step(self):
        pass
