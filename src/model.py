import random
import math

from agent import Agent
#from environment import grid, env_cell
import environment

'''
    Change only the value of masterHeight to change the dimensions of the grid
        because it must always be a square.
'''

masterHeight = 10
masterWidth = masterHeight
#masterWidth = 52

class SlimeModel():
    def __init__(self, height, width):
        # number of agents per tile
        self.n = 1
        # grid density
        self.gD = 0.5
        # rate of cAMP decay
        self.k = 0.1
        # diffusion constant of cAMP
        self.Dc = 0.1
        # spatial resolution for cAMP simulation
        self.Dh = 0.1
        # time resolution for cAMP simulation
        self.Dt = 1
        # rate of cAMP secretion by an agent
        self.f = 1
        # number of rows/columns in spatial array
        self.w = width

        # height of grid
        self.height = height
        # width of grid
        self.width = width

        # Counter for generating sequential unique id's
        self.j = 0

        # Create grid (of type MultiGrid to support multiple agents per cell
        self.grid = environment.grid(self.width, self.height)

        # Initialize for iterating through columns (x) and rows (y)
        self.x = 0
        self.y = 0

        # Variable for storing random numbers
        r = 0
    
        init_iterator = iter(self.grid) 

        # Initial loop to create agents and fill agents list with them
        for grid_cell in range(self.grid.get_n_cells()):
            cell = next(init_iterator)
            # Add random amoutn of cAMP to cell (<1)
            cell.add_value(random.random())
            x = cell.x
            y = cell.y

            # Loop to create SlimeAgents
            if self.gD % 1 != 0:
                r = random.random()
                if r <= self.gD:
                    for i in range(self.n):
                        # Create object of type SlimeAgent
                        ag = Agent(x, y)
                        # Set agent's sec_rate to 5
                        ag.set_contents("sec_rate", 5)
                        # Place agent onto grid at coordinates x, y
                        cell.add_agent(ag)
            else:
                for i in range(self.n):
                    # Create object of type SlimeAgent
                    ag = Agent(x, y)
                    # Set agent's sec_rate to 5
                    ag.set_contents("sec_rate", 5)
                    # Place agent onto grid at coordinates x, y
                    cell.add_agent(ag)

    def export_env_to_csv(self, iteration):
        self.grid.export_env_to_csv(iteration)

    def export_agents_to_csv(self, iteration):
        self.grid.export_agents_to_csv(iteration)
    
    # Step method
    def step(self):
        cNeighbors = list()
        neighbors = list()
        lap = 0
        amtSelf = 0
        newDiag = 0
        oldDiag = 0
        nAgents = 0
        layer = 1
        secRate = 0
        

        iterator = iter(self.grid)

        ''' Perform cAMP decay and diffusion actions '''
        for grid_cell in range(self.grid.get_n_cells()):
            cell = next(iterator)
            # Reset lap to 0
            lap = 0

            agents = cell.get_agents()
            # Set neighbors to cAMPobj's neighbors (Von Neumann)
            if len(agents) != 0:
                cNeighbors = self.grid.get_neighbors(agents[0], False)
            # Add cAMP objects from neighbors to cNeighbors
            for neighbor in cNeighbors:
                neighbors.append(neighbor)

            # Add sum of neighbors to lap
            for mol in cNeighbors:
                lap += mol.get_value()

            curr_cell_amt = cell.get_value()
            # Reassign lap to the laplacian (using previous neighbor sum value)
            lap = (lap - 4 * curr_cell_amt)/(self.Dh**2)
            # Add decay to current cAMP object
            cell.add_value((-self.k * curr_cell_amt + self.Dc * lap) * self.Dt)

            # Wipe cNeighbors
            cNeighbors.clear()


            # Iterate through all contents of a grid cell
            for agent in agents:
                # Get all neighbors (excuding self)
                neighbors = self.grid.get_neighbors_at(cell.x, cell.y, False)

                # Add cAMP secretion to the cell that the agent shares with a cAMP object
                cell.add_value(agent.get_contents_at("sec_rate") * self.Dt)
                # Decide whether or not to move
                newx = (cell.x + random.randint(-1, 2)) % self.w
                newy = (cell.y + random.randint(-1, 2)) % self.w

                # Calculate differences
                newDiag = self.grid.get_cell(newx-1, newy-1).get_value()
                diff = self.grid.get_cell(cell.x-1, cell.y-1).get_value()

                # Fix if there are crazy values for diff
                if diff > 10:
                    diff = 10
                elif diff < -10:
                    diff = -10

                # Decide to move
                if random.random() < math.exp(diff) / (1 + math.exp(diff)):
                    self.grid.move_agent(agent, newx, newy)


