import csv
import random
from agent import Agent

class env_cell():
    def __init__(self, x, y, value_param):
        self.x = x
        self.y = y
        self.value = value_param
        self.contents = list()

    def get_value(self):
        return self.value

    def get_agents(self):
        return self.contents

    def add_value(self, amount):
        self.value += amount

    def add_agent(self, agent):
        self.contents.append(agent)


class grid():
    def __init__(self, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.size = width_param * height_param
        self.grid = [[env_cell(x, y, 0) for x in range(self.width)] for y in range(self.height)]
        self.iter_x = 0
        self.iter_y = 0

    def get_agent(self, x, y):
        return self.grid[x][y].contents

    def get_cell(self, x, y):
        return self.grid[x][y]

    def get_n_cells(self):
        return self.width * self.height

    ''' ITERATION '''
    def __iter__(self):
        return self

    def __next__(self):
        curr_x = self.iter_x
        curr_y = self.iter_y

        if curr_x == self.width:
            curr_y += 1
            curr_x = 0

        if curr_y == self.height:
            curr_y = 0
            curr_x = 0

        self.iter_x = curr_x + 1
        self.iter_y = curr_y

        return self.grid[curr_x][self.iter_y]


    ''' MODEL METHODS '''
    
    def move_agent(self, agent, target_x, target_y):
        agents_at_pos = self.grid[agent.position[0]][agent.position[1]].contents
        for ag in agents_at_pos:
            if(ag == agent):
                self.grid[target_x][target_y].add_agent(agent)
                self.grid[agent.position[0]][agent.position[1]].contents.remove(agent)

    def get_neighbors(self, agent, moore):
        x = agent.position[0]
        y = agent.position[1]

        neighbors = list()

        '''if moore == True:
            if x+1 < self.width:
                neighbors.append(self.grid[x+1][y])
                if y+1 < self.height:
                    neighbors.append(self.grid[x+1][y+1])
                if y-1 >= 0:
                    neighbors.append(self.grid[x+1][y-1])
            if x-1 >= 0:
                neighbors.append(self.grid[x-1][y])
                if y+1 < self.height:
                    neighbors.append(self.grid[x-1][y+1])
                if y-1 >= 0:
                    neighbors.append(self.grid[x-1][y-1])
            if y+1 < self.height:
                neighbors.append(self.grid[x][y+1])
            if y-1 >= 0:
                neighbors.append(self.grid[x][y-1])
        else:'''
        if x+1 < self.width:
            neighbors.append(self.grid[x+1][y])
        if x-1 >= 0:
            neighbors.append(self.grid[x-1][y])
        if y+1 < self.height:
            neighbors.append(self.grid[x][y+1])
        if y-1 < self.height:
            neighbors.append(self.grid[x][y-1])
            
        return neighbors

    def get_neighbors_at(self, x, y, moore):
        neighbors = list()
        
        '''if moore == True:
            if x+1 < self.width:
                neighbors.append(self.grid[x+1][y])
                if y+1 < self.height:
                    neighbors.append(self.grid[x+1][y+1])
                if y-1 >= 0:
                    neighbors.append(self.grid[x+1][y-1])
            if x-1 >= 0:
                neighbors.append(self.grid[x-1][y])
                if y+1 < self.height:
                    neighbors.append(self.grid[x-1][y+1])
                if y-1 >= 0:
                    neighbors.append(self.grid[x-1][y-1])
            if y+1 < self.height:
                neighbors.append(self.grid[x][y+1])
            if y-1 >= 0:
                neighbors.append(self.grid[x][y-1])
        else:'''
        if x+1 < self.width:
            neighbors.append(self.grid[x+1][y])
        if x-1 >= 0:
            neighbors.append(self.grid[x-1][y])
        if y+1 < self.height:
            neighbors.append(self.grid[x][y+1])
        if y-1 < self.height:
            neighbors.append(self.grid[x][y-1])
        
            
        return neighbors

    def find(self, param, value):
        for y in range(self.height):
            for x in range(self.width):
                contents = self.grid[x][y].contents
                for ag in contents:
                    if ag.get_contents_at(param) == value:
                        return ag
        return None

    def find_all(self, param, value):
        found_agents = list()
        for y in range(self.height):
            for x in range(self.width):
                contents = self.grid[x][y].contents
                for ag in contents:
                    if ag.get_contents_at(param) == value:
                        found_agents.append(ag)

        return found_agents

    ''' EXPORTING '''

    def print_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.grid[x][y].value, end=" | ")
            print("")

    def export_env_to_csv(self, iteration):
        with open("output/environment/environment_" + str(iteration) + ".csv", "w", newline="") as outfile:
            writer = csv.writer(outfile)
            row = list()
            for y in range(self.height):
                for x in range(self.width):
                    row.append(self.grid[x][y].value)
                writer.writerow(row)
                row = list()

    def export_agents_to_csv(self, iteration):
        with open("output/agents/agents_" + str(iteration) + ".csv", "w", newline="") as outfile:
            writer = csv.writer(outfile)
            row = list()
            for y in range(self.height):
                for x in range(self.width):
                    row.append([ag.get_contents_at("value") for ag in self.grid[x][y].contents])
                writer.writerow(row)
                row = list()
            
    def random_init(self, low_bound, up_bound):
        for y in range(self.height):
            for x in range(self.width):
                agent = Agent(x, y)
                agent.set_contents("value", random.randint(low_bound, up_bound))
                self.grid[x][y].add_agent(agent)
        
